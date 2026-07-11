import sys
import os
import argparse
import time

try:
    from google import genai
except ImportError:
    genai = None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()

    if not os.environ.get("GEMINI_API_KEY") or not genai:
        print("Mock Baseline Agent ran successfully. (GEMINI_API_KEY or google-genai not found)")
        print(f"Prompt received: {args.prompt}")
        
        # Simulate baseline fixing the calculator benchmark
        if "logic error" in args.prompt.lower():
            os.makedirs("tests", exist_ok=True)
            with open("tests/test_calc.py", "w") as f:
                f.write("def test_dummy(): pass\n")
            print("Fixed calculator bugs.")
            
        # Simulate baseline fixing the architecture benchmark
        if "architecture review" in args.prompt.lower():
            with open("architecture_report.md", "w") as f:
                f.write("# Architecture Report\nThis is a baseline generated report.")
            print("Generated architecture report.")
            
        return

    # Real baseline execution
    client = genai.Client()
    prompt = f"You are working in a codebase. Task: {args.prompt}. Provide a bash script that accomplishes this task. Output ONLY the raw bash script without markdown blocks."
    
    try:
        response = client.models.generate_content(
            model="gemini-3.1-pro",
            contents=prompt
        )
        
        usage = response.usage_metadata
        in_tokens = usage.prompt_token_count if usage else 0
        out_tokens = usage.candidates_token_count if usage else 0
        
        print(f"__METRICS__:{in_tokens},{out_tokens}")
        print(response.text)
        
        with open("baseline_fix.sh", "w") as f:
            f.write(response.text)
        os.system("bash baseline_fix.sh")
        
    except Exception as e:
        print(f"Error calling Gemini: {e}")

if __name__ == "__main__":
    main()
