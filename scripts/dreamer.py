import time
import argparse
import logging
import sys
import atexit
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("EsperDreamer")

def compress_memory(memory_dir: Path, window_size: int):
    logger.info(f"Checking for old memory files to compress in {memory_dir} (window size: {window_size})...")
    files = list(memory_dir.glob("*.md"))
    files.sort(key=lambda p: p.stat().st_mtime)
    
    if len(files) > window_size:
        stale_files = files if window_size == 0 else files[:-window_size]
        for file in stale_files:
            logger.info(f"Pruning stale context file: {file}")
            file.unlink()
        logger.info(f"Memory compression complete. Pruned {len(stale_files)} files. Kept {window_size} files.")
    else:
        logger.info(f"Memory compression complete. No files to prune. Within window size ({len(files)} <= {window_size}).")

def synthesize_knowledge_graph(kg_path: Path):
    logger.info("Knowledge graph synthesis is not yet implemented. Skipping.")

def dream(frequency: int, window_size: int):
    esper_dir = Path(".esper")
    memory_dir = esper_dir / "shared_context"
    kg_path = esper_dir / "knowledge_graph.json"
    
    esper_dir.mkdir(parents=True, exist_ok=True)
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    lock_file = esper_dir / ".dreamer.lock"
    if lock_file.exists():
        logger.info("Lock file exists. Another dreamer instance is running. Exiting.")
        sys.exit(0)
        
    lock_file.touch()
    
    def remove_lock():
        if lock_file.exists():
            lock_file.unlink()
            
    atexit.register(remove_lock)

    logger.info(f"Starting Asynchronous Dreaming loop with a frequency of {frequency} seconds.")

    while True:
        try:
            logger.info("Dreamer waking up to process memory and context...")
            compress_memory(memory_dir, window_size)
            synthesize_knowledge_graph(kg_path)
            logger.info(f"Dream cycle finished. Sleeping for {frequency} seconds.")
            time.sleep(frequency)
        except KeyboardInterrupt:
            logger.info("Dreamer received shutdown signal. Exiting.")
            break
        except Exception as e:
            logger.error(f"Error during dreaming cycle: {e}")
            logger.info("Retrying in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Esper Asynchronous Dreamer Daemon")
    parser.add_argument(
        "--frequency",
        type=int,
        default=86400,
        help="Frequency in seconds to run the dream cycle (default: 86400 for 24 hours)"
    )
    parser.add_argument(
        "--window-size",
        type=int,
        default=10,
        help="Number of memory files to keep (default: 10)"
    )
    args = parser.parse_args()

    dream(args.frequency, args.window_size)
