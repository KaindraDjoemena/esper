import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Esper Policy Gate Validation Script')
    parser.add_argument('--action', required=True, help='The intended action')
    parser.add_argument('--target', required=True, help='The target of the action')
    args = parser.parse_args()

    high_risk_actions = ['delete', 'bulk_edit', 'wipe', 'overwrite_all', 'rm', 'rmdir']

    if args.action.lower() in high_risk_actions:
        print("> [!WARNING]")
        print(f"> The action '{args.action}' on target '{args.target}' is flagged as high-risk by the Esper Policy Gate.")
        print("> You MUST use the native `ask_question` interactive modal tool to get undeniable user approval before proceeding.")
        print("> Do not proceed without explicit user confirmation.")
        sys.exit(1)  # Graceful exit to avoid crashing the agent

    print(f"Action '{args.action}' on target '{args.target}' is permitted.")
    sys.exit(0)

if __name__ == '__main__':
    main()
