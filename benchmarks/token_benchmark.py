import os
import glob

try:
    from google import genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def count_tokens(text):
    # Try using Gemini API native token counting if key is present
    if HAS_GENAI and os.environ.get("GEMINI_API_KEY"):
        try:
            client = genai.Client()
            # We use gemini-1.5-pro for token counting as it is standard, or whatever is accessible
            response = client.models.count_tokens(model="gemini-1.5-pro", contents=text)
            return response.total_tokens
        except Exception as e:
            print(f"[Warning] API token counting failed: {e}. Falling back to heuristic.")
    
    # Fallback heuristic: 1 token is roughly 4 characters
    return int(len(text) / 4)

def get_esper_files(base_dir):
    files = []
    for root, _, filenames in os.walk(base_dir):
        # Exclude non-core directories
        if any(exclude in root for exclude in ["benchmarks", "shared_context", "bootstrap", ".git"]):
            continue
        for filename in filenames:
            if filename.endswith(".md") and filename != "README.md":
                files.append(os.path.join(root, filename))
    return files

def parse_dependencies(filepath, base_dir, visited=None):
    if visited is None:
        visited = set()
    
    if filepath in visited or not os.path.exists(filepath):
        return []
        
    visited.add(filepath)
    deps = [filepath]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    in_deps = False
    for line in content.split('\n'):
        if line.startswith("## Required Dependencies"):
            in_deps = True
            continue
        if in_deps and line.startswith("## "):
            in_deps = False
        
        if in_deps and line.strip().startswith("- "):
            dep_path = line.strip()[2:].split(' ')[0] # Extract path before any comments
            full_dep_path = os.path.join(base_dir, dep_path)
            if full_dep_path not in visited:
                deps.extend(parse_dependencies(full_dep_path, base_dir, visited))
                
    return deps

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # 1. Monolith Token Count
    all_files = get_esper_files(base_dir)
    monolith_text = ""
    for f in all_files:
        with open(f, 'r', encoding='utf-8') as file:
            monolith_text += file.read() + "\n"
    monolith_tokens = count_tokens(monolith_text)
    
    # 2. Esper Dynamic Context (Example: feature.md)
    entry_point = os.path.join(base_dir, "prompts", "feature.md")
    esper_files = parse_dependencies(entry_point, base_dir)
    esper_text = ""
    for f in esper_files:
        with open(f, 'r', encoding='utf-8') as file:
            esper_text += file.read() + "\n"
    esper_tokens = count_tokens(esper_text)
    
    # 3. Normal Prompt
    normal_prompt_path = os.path.join(base_dir, "benchmarks", "baselines", "normal_feature.md")
    if os.path.exists(normal_prompt_path):
        with open(normal_prompt_path, 'r', encoding='utf-8') as file:
            normal_text = file.read()
        normal_tokens = count_tokens(normal_text)
    else:
        normal_tokens = 0
        
    print("\n=== Token Benchmark Results ===")
    if HAS_GENAI and os.environ.get("GEMINI_API_KEY"):
        print("Tokenizer: Gemini API Native (google-genai)")
    else:
        print("Tokenizer: Heuristic Fallback (characters / 4) -> Set GEMINI_API_KEY for true count")
        
    print(f"\n1. Normal Prompt (Baseline):   {normal_tokens} tokens")
    print(f"2. Esper Dynamic (Feature):  {esper_tokens} tokens")
    print(f"3. Monolithic Prompt:        {monolith_tokens} tokens")
    
    print("\n=== Efficiency Analysis ===")
    if monolith_tokens > 0:
        saved = 100 - (esper_tokens/monolith_tokens)*100
        print(f"- Esper saves {saved:.1f}% tokens compared to loading the whole framework as a Monolith.")
    if normal_tokens > 0:
        ratio = esper_tokens/normal_tokens
        print(f"- Esper uses {ratio:.1f}x the tokens of a 'normal' prompt.")
        print("  (This represents the tradeoff: investing more context for Esper's checklists/principles to guarantee quality and safety).")

if __name__ == "__main__":
    main()
