import docker
import yaml
import sys
import os
import time

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def load_schema(filepath="schema.yaml"):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)

def run_benchmark(test_case, client, mode="esper"):
    print(f"\n--- Running Benchmark: {test_case['id']} ({mode.upper()}) ---")
    
    repo_url = test_case['repository']
    commit = test_case['commit_hash']
    prompt = test_case['esper_prompt']
    verify_cmd = test_case['verification']['command']
    expected_code = test_case['verification'].get('expected_exit_code', 0)
    
    try:
        container = client.containers.run(
            "esper-sandbox:latest",
            name=f"esper-test-{test_case['id']}-{mode}",
            detach=True,
            working_dir="/workspace",
            environment={"GEMINI_API_KEY": os.environ.get("GEMINI_API_KEY", "")}
        )
    except Exception as e:
        print(f"Failed to start sandbox container: {e}")
        return None
    
    metrics = {"latency": 0.0, "in_tokens": 0, "out_tokens": 0, "correct": False, "agent_output": "", "verify_output": ""}
    
    try:
        container.exec_run(f"git clone {repo_url} .")
        if commit != "HEAD":
            container.exec_run(f"git checkout {commit}")
            
        start_time = time.time()
        
        if mode == "esper":
            cmd = f"/bin/bash -c \"set -o pipefail; esper '{prompt}' 2>&1 | tee /proc/1/fd/1\""
        else:
            cmd = f"/bin/bash -c \"set -o pipefail; python3 /usr/local/bin/baseline_agent.py --prompt '{prompt}' 2>&1 | tee /proc/1/fd/1\""
            
        exit_code, output = container.exec_run(cmd)
        
        metrics["latency"] = time.time() - start_time
        metrics["agent_output"] = output.decode('utf-8').strip()
        
        # Parse tokens if baseline mock prints them
        for line in metrics["agent_output"].split('\n'):
            if line.startswith("__METRICS__:"):
                parts = line.split(":", 1)[1].split(",")
                metrics["in_tokens"] = int(parts[0])
                metrics["out_tokens"] = int(parts[1])
        
        exit_code, verify_output = container.exec_run(f"/bin/bash -c \"set -o pipefail; {verify_cmd} 2>&1 | tee /proc/1/fd/1\"")
        metrics["verify_output"] = verify_output.decode('utf-8').strip()
        
        if exit_code == expected_code:
            metrics["correct"] = True
            print(f"✅ {mode.upper()} PASSED: {test_case['id']}")
        else:
            print(f"❌ {mode.upper()} FAILED: {test_case['id']} (Exit Code: {exit_code})")
            
        return metrics
    finally:
        container.stop()
        container.remove()

def generate_report(results):
    report_path = "benchmark_report.md"
    with open(report_path, "w") as f:
        f.write("# Esper vs Baseline Gemini Benchmark Report\n\n")
        f.write("Evaluate the quality of the outputs manually.\n\n")
        for test_id, data in results.items():
            f.write(f"## Test: {test_id}\n\n")
            
            f.write("### Baseline Gemini\n")
            if data['baseline']:
                b_metrics = data['baseline']
                f.write(f"- Correctness: {'✅ Pass' if b_metrics['correct'] else '❌ Fail'}\n")
                f.write(f"- Latency: {b_metrics['latency']:.2f}s\n")
                if b_metrics['in_tokens'] > 0:
                    f.write(f"- Input Tokens: {b_metrics['in_tokens']}\n")
                    f.write(f"- Output Tokens: {b_metrics['out_tokens']}\n")
                f.write("#### Output\n```text\n" + b_metrics['agent_output'] + "\n```\n\n")
                f.write("#### Verification\n```text\n" + b_metrics['verify_output'] + "\n```\n\n")
            else:
                f.write("Failed to run.\n\n")
            
            f.write("### Esper Agent\n")
            if data['esper']:
                e_metrics = data['esper']
                f.write(f"- Correctness: {'✅ Pass' if e_metrics['correct'] else '❌ Fail'}\n")
                f.write(f"- Latency: {e_metrics['latency']:.2f}s\n")
                f.write("#### Output\n```text\n" + e_metrics['agent_output'] + "\n```\n\n")
                f.write("#### Verification\n```text\n" + e_metrics['verify_output'] + "\n```\n\n")
            else:
                f.write("Failed to run.\n\n")
            f.write("---\n")
    print(f"Report generated at {os.path.abspath(report_path)}")
    return os.path.abspath(report_path)

def main():
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Failed to connect to Docker daemon: {e}")
        sys.exit(1)
        
    schema_path = os.path.join(os.path.dirname(__file__), "schema.yaml")
    config = load_schema(schema_path)
    test_cases = config.get("test_cases", [])
    
    dockerfile_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(os.path.dirname(dockerfile_dir))
    
    try:
        print("Building esper-sandbox:latest...")
        image, build_logs = client.images.build(
            path=project_root,
            dockerfile="esper/benchmarks/Dockerfile.eval",
            tag="esper-sandbox:latest",
            rm=True
        )
    except Exception as e:
        print(f"Failed to build Docker image: {e}")
        sys.exit(1)
    
    results = {}
    for test in test_cases:
        test_id = test['id']
        results[test_id] = {}
        results[test_id]['baseline'] = run_benchmark(test, client, mode="baseline")
        results[test_id]['esper'] = run_benchmark(test, client, mode="esper")
            
    generate_report(results)

if __name__ == "__main__":
    main()
