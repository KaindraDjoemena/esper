import sys
import json
import argparse
try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

def main():
    parser = argparse.ArgumentParser(description="Validate JSON against A2A contract schema.")
    parser.add_argument("json_file", help="Path to the JSON file to validate")
    parser.add_argument("--retry-count", type=int, default=0, help="Number of retry attempts")
    args = parser.parse_args()

    schema_path = "C:/Users/KD/.gemini/esper/templates/a2a-contract.json"
    
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except Exception as e:
        print(f"Error loading schema: {e}")
        sys.exit(1)
        
    try:
        with open(args.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        if args.retry_count >= 3:
            print("Max retries reached (>= 3). Hard-crashing the workflow.")
            sys.exit(1)
        print(f"Retry count is {args.retry_count}. Please reflect on the errors and try again.")
        sys.exit(0)
        
    errors = []
    if HAS_JSONSCHEMA:
        validator = jsonschema.Draft7Validator(schema)
        errors = [f"Path {list(e.path)}: {e.message}" for e in validator.iter_errors(data)]
    else:
        # Basic manual validation based on the schema if jsonschema is not installed
        required_keys = ["task_id", "task_type", "payload", "status"]
        for key in required_keys:
            if key not in data:
                errors.append(f"Missing required key: {key}")
        if "task_type" in data and data["task_type"] not in ["plan", "execute", "review", "synthesize"]:
            errors.append(f"Invalid task_type: {data['task_type']}")
        if "status" in data and data["status"] not in ["pending", "in_progress", "completed", "failed"]:
            errors.append(f"Invalid status: {data['status']}")

    if not errors:
        print("Validation successful.")
        sys.exit(0)
        
    print(f"Validation failed with {len(errors)} error(s):")
    for error in errors:
        print(f" - {error}")
        
    if args.retry_count >= 3:
        print("Max retries reached (>= 3). Hard-crashing the workflow.")
        sys.exit(1)
    else:
        print(f"Retry count is {args.retry_count}. Please reflect on the errors and try again.")
        sys.exit(0)

if __name__ == "__main__":
    main()
