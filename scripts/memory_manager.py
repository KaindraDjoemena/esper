import argparse
import os
import glob

def parse_args():
    parser = argparse.ArgumentParser(description="Lifecycle Memory Management for Esper")
    parser.add_argument('--window-size', type=int, default=10, help="Sliding window size in days or operations")
    parser.add_argument('--context-dir', type=str, default=".esper/shared_context/", help="Path to shared context directory")
    parser.add_argument('--prune', action='store_true', help="Execute selective forgetting (prune stale context files)")
    return parser.parse_args()

def prune_stale_files(context_dir, window_size):
    if not os.path.exists(context_dir):
        print(f"Context directory {context_dir} does not exist.")
        return
    files = glob.glob(os.path.join(context_dir, "*.md"))
    # In a real implementation, this would use stat() for timestamps or a metadata index
    # Here we simulate pruning logic based on deterministic sorting (e.g. oldest first)
    files.sort(key=os.path.getmtime)
    
    if len(files) > window_size:
        stale_files = files if window_size == 0 else files[:-window_size]
        for file in stale_files:
            print(f"Pruning stale context file: {file}")
            os.remove(file)
        print(f"Pruned {len(stale_files)} files. Kept {window_size} files.")
    else:
        print("No files to prune. Within window size.")

def main():
    args = parse_args()
    print("Running Lifecycle Memory Management...")
    if args.prune:
        prune_stale_files(args.context_dir, args.window_size)
    else:
        print("Run with --prune to execute selective forgetting.")

if __name__ == "__main__":
    main()
