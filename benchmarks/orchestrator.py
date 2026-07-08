import docker
import yaml
import sys
import os

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def load_schema(filepath="schema.yaml"):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)

def run_benchmark(test_case, client):
    print(f"\n--- Running Benchmark: {test_case['id']} ---")
    print(f"Description: {test_case['description']}")
    
    # Configuration
    repo_url = test_case['repository']
    commit = test_case['commit_hash']
    prompt = test_case['esper_prompt']
    verify_cmd = test_case['verification']['command']
    expected_code = test_case['verification'].get('expected_exit_code', 0)
    
    # 1. Setup Docker Container
    # We now use our custom built esper-sandbox image!
    try:
        container = client.containers.run(
            "esper-sandbox:latest",
            name=f"esper-test-{test_case['id']}",
            detach=True,
            working_dir="/workspace"
        )
        print(f"Container created:\n  Name: esper-test-{test_case['id']}\n  ID: {container.id[:12]}\n  Image: esper-sandbox:latest")
    except Exception as e:
        print(f"Failed to start sandbox container: {e}")
        return False
    
    try:
        # Clone repo
        print(f"Cloning repository {repo_url} at commit {commit}...")
        container.exec_run(f"git clone {repo_url} .")
        if commit != "HEAD":
            container.exec_run(f"git checkout {commit}")
            
        # 2. Run Esper 
        print(f"Executing Esper with prompt: '{prompt}'...")
        exit_code, output = container.exec_run(f"/bin/bash -c \"set -o pipefail; esper run --prompt '{prompt}' 2>&1 | tee /proc/1/fd/1\"")
        
        # 3. Verification (End-State Validation)
        print(f"Running verification command: '{verify_cmd}'...")
        exit_code, output = container.exec_run(f"/bin/bash -c \"set -o pipefail; {verify_cmd} 2>&1 | tee /proc/1/fd/1\"")
        
        print("\n[Verification Output]")
        print(output.decode('utf-8').strip())
        
        if exit_code == expected_code:
            print(f"✅ PASSED: {test_case['id']}")
            return True
        else:
            print(f"❌ FAILED: {test_case['id']} (Exit Code: {exit_code})")
            return False
            
    finally:
        print("Cleaning up container...")
        container.stop()
        container.remove()

def main():
    print("Starting Esper Benchmarking Orchestrator...")
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Failed to connect to Docker daemon: {e}")
        print("Ensure Docker Desktop is running.")
        sys.exit(1)
        
    schema_path = os.path.join(os.path.dirname(__file__), "schema.yaml")
    if not os.path.exists(schema_path):
        print(f"Error: Could not find {schema_path}")
        sys.exit(1)
        
    config = load_schema(schema_path)
    test_cases = config.get("test_cases", [])
    
    # Build the custom Docker sandbox image
    print("\nBuilding Docker sandbox image 'esper-sandbox:latest' (this may take a moment)...")
    dockerfile_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(os.path.dirname(dockerfile_dir))
    try:
        image, build_logs = client.images.build(
            path=project_root,
            dockerfile="esper/benchmarks/Dockerfile.eval",
            tag="esper-sandbox:latest",
            rm=True
        )
        for chunk in build_logs:
            if 'stream' in chunk:
                print(chunk['stream'].strip())
        print("Sandbox image built successfully!")
    except Exception as e:
        print(f"Failed to build Docker image: {e}")
        sys.exit(1)
    
    passed = 0
    for test in test_cases:
        if run_benchmark(test, client):
            passed += 1
            
    print(f"\n=== Benchmark Summary ===")
    print(f"Total: {len(test_cases)} | Passed: {passed} | Failed: {len(test_cases) - passed}")

if __name__ == "__main__":
    main()
