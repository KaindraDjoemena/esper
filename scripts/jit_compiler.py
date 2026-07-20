import os
import sys
import re
import argparse
import xml.etree.ElementTree as ET

def read_keywords_from_frontmatter(abs_filepath):
    if not os.path.exists(abs_filepath):
        return []
    try:
        with open(abs_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            kw_match = re.search(r'^keywords:\s*\[(.*?)\]', frontmatter, re.MULTILINE)
            if kw_match:
                return [k.strip() for k in kw_match.group(1).split(',')]
    except Exception:
        pass
    return []

def resolve_path(base_dir, filepath):
    return os.path.normpath(os.path.join(base_dir, filepath))

def parse_dependencies(content):
    required = []
    optional = []
    
    # Extract the <esper_module> blocks since the file mixes markdown and XML
    for module_match in re.finditer(r'<esper_module[^>]*>.*?</esper_module>', content, re.DOTALL):
        try:
            root = ET.fromstring(module_match.group(0))
            for req in root.findall('.//required/item'):
                if req.text:
                    required.append(req.text.strip())
            for opt in root.findall('.//optional/item'):
                if opt.text:
                    optional.append(opt.text.strip())
        except ET.ParseError:
            pass
            
    return required, optional

def should_include_optional(filepath, user_prompt, base_dir):
    if not user_prompt:
        return False
        
    abs_path = resolve_path(base_dir, filepath)
    keywords = read_keywords_from_frontmatter(abs_path)
    prompt_lower = user_prompt.lower()
    for kw in keywords:
        if kw in prompt_lower:
            return True
    return False

def get_project_overrides(target_dir):
    blocks = []
    
    # Check for AGENTS.md
    agents_md_path = os.path.join(target_dir, "AGENTS.md")
    if os.path.exists(agents_md_path):
        with open(agents_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        blocks.append(f"<esper_context source=\"AGENTS.md\">\n{content}\n</esper_context>")
        
    # Check for .esper/shared_context/ files
    shared_context_dir = os.path.join(target_dir, ".esper", "shared_context")
    if os.path.exists(shared_context_dir) and os.path.isdir(shared_context_dir):
        for root, _, files in os.walk(shared_context_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, target_dir).replace('\\', '/')
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    blocks.append(f"<esper_context source=\"{rel_path}\">\n{content}\n</esper_context>")
                    
    if blocks:
        return "<!-- PROJECT OVERRIDES -->\n" + "\n\n".join(blocks)
    return ""

def compile_context(entry_point, base_dir, user_prompt="", target_dir="."):
    visited = set()
    skipped_optional = set()
    output_blocks = []
    
    def traverse(filepath):
        norm_filepath = filepath.replace('\\', '/')
        if norm_filepath in visited:
            return
            
        abs_path = resolve_path(base_dir, filepath)
        if not os.path.exists(abs_path):
            output_blocks.append(f"> [!WARNING]\n> **Missing Dependency**: The required dependency `{filepath}` could not be found and was skipped. Proceed with caution as you may be missing critical context.")
            return
            
        visited.add(norm_filepath)
        
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        required, optional = parse_dependencies(content)
        
        # Traverse required dependencies first
        for req in required:
            traverse(req)
            
        # Evaluate optional dependencies
        for opt in optional:
            if should_include_optional(opt, user_prompt, base_dir):
                traverse(opt)
            else:
                skipped_optional.add(opt.replace('\\', '/'))
                
        # Append the current file's content
        # Post-order traversal ensures dependencies appear before the file that requires them
        output_blocks.append(f"<esper_context source=\"{norm_filepath}\">\n{content}\n</esper_context>")

    traverse(entry_point)
    
    final_output = "\n\n".join(output_blocks)
    
    overrides = get_project_overrides(target_dir)
    if overrides:
        final_output += "\n\n" + overrides
    
    if skipped_optional:
        discovery_block = "> [!TIP]\n> The following optional modules were not pre-loaded, but you may read them if you determine they are necessary during your task:\n"
        for skipped in sorted(list(skipped_optional)):
            discovery_block += f"> - `{skipped}`\n"
        final_output += "\n\n" + discovery_block
        
    return final_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JIT Compiler for Esper")
    parser.add_argument("entry_point", help="Relative path to the entry point (e.g., prompts/architecture-review.md)")
    parser.add_argument("--prompt", "-p", default="", help="User's initial prompt for heuristic matching")
    parser.add_argument("--target-dir", "-t", default=".", help="Target project directory to check for AGENTS.md and .esper/shared_context")
    
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    compiled_text = compile_context(args.entry_point, base_dir, args.prompt, args.target_dir)
    print(compiled_text)
    
    lock_path = os.path.join(args.target_dir, ".esper", ".dreamer.lock")
    if not os.path.exists(lock_path):
        import subprocess
        dreamer_script = os.path.join(base_dir, "scripts", "dreamer.py")
        subprocess.Popen([sys.executable, dreamer_script])
