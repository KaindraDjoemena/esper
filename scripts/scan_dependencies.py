import os
import re
import json
import argparse
from pathlib import Path

def normalize_path(repo_root, base_file_rel, link_path):
    if link_path.startswith('/'):
        return link_path.lstrip('/')
        
    repo_root_path = Path(repo_root).resolve()
    base_dir = (repo_root_path / base_file_rel).parent
    
    if link_path.startswith('./') or link_path.startswith('../'):
        try:
            resolved = (base_dir / link_path).resolve()
            if resolved.is_relative_to(repo_root_path):
                return resolved.relative_to(repo_root_path).as_posix()
        except Exception:
            pass
    else:
        try:
            resolved_dir = (base_dir / link_path).resolve()
            if resolved_dir.is_relative_to(repo_root_path) and resolved_dir.exists():
                return resolved_dir.relative_to(repo_root_path).as_posix()
        except Exception:
            pass
            
        try:
            resolved_root = (repo_root_path / link_path).resolve()
            if resolved_root.is_relative_to(repo_root_path):
                return resolved_root.relative_to(repo_root_path).as_posix()
        except Exception:
            pass

    return link_path

def scan_dependencies(repo_root):
    root_path = Path(repo_root).resolve()
    
    all_md_files = set()
    dependencies_map = {}
    
    ENTRY_POINTS = {'routing.md', 'index.md', 'readme.md', 'changelog.md', 'agents.md'}
    
    for filepath in root_path.rglob('*.md'):
        rel_path_obj = filepath.relative_to(root_path)
        if any(part.startswith('.') and part != '.' for part in rel_path_obj.parts):
            continue
        rel_path = rel_path_obj.as_posix()
        all_md_files.add(rel_path)
        dependencies_map[rel_path] = {
            'required': [],
            'optional': [],
            'canonical': [],
            'inline': []
        }

    list_item_pattern = re.compile(r'^\s*-\s+([^\s\)]+\.md)(?:\s.*)?$')
    inline_link_pattern = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:#[^)]*)?\)')

    for file_rel in all_md_files:
        file_path = root_path / file_rel
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception:
            continue
            
        current_section = None
        
        for line in lines:
            if line.startswith('## Required Dependencies'):
                current_section = 'required'
                continue
            elif line.startswith('## Optional Dependencies'):
                current_section = 'optional'
                continue
            elif line.startswith('## Canonical Sources'):
                current_section = 'canonical'
                continue
            elif line.startswith('#'):
                current_section = None

            if current_section:
                match = list_item_pattern.match(line)
                if match:
                    dep = match.group(1)
                    norm_dep = normalize_path(root_path, file_rel, dep)
                    dependencies_map[file_rel][current_section].append(norm_dep)

        for match in inline_link_pattern.finditer(content):
            dep = match.group(1)
            if dep.startswith('http://') or dep.startswith('https://'):
                continue
            norm_dep = normalize_path(root_path, file_rel, dep)
            dependencies_map[file_rel]['inline'].append(norm_dep)

    broken_links = []
    referenced_files = set()
    
    for file_rel, deps in dependencies_map.items():
        for dep_type, dep_list in deps.items():
            for target in dep_list:
                referenced_files.add(target)
                if target not in all_md_files:
                    broken_links.append({
                        'source': file_rel,
                        'target': target,
                        'type': dep_type
                    })

    orphaned_files = []
    for file_rel in all_md_files:
        if file_rel not in referenced_files:
            if Path(file_rel).name.lower() not in ENTRY_POINTS:
                orphaned_files.append(file_rel)

    results = {
        'total_files': len(all_md_files),
        'orphaned_files': sorted(orphaned_files),
        'broken_links': broken_links,
        'dependencies': dependencies_map
    }
    
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan Esper dependencies.')
    parser.add_argument('--repo-root', default='.', help='Path to repo root')
    args = parser.parse_args()
    
    res = scan_dependencies(args.repo_root)
    print(json.dumps(res, indent=2))
