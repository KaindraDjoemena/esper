import os
import re

files = [
    r'C:\Users\KD\.gemini\esper\.agents\rules\esper-philosophy.md',
    r'C:\Users\KD\.gemini\esper\.agents\rules\esper-rpc.md',
    r'C:\Users\KD\.gemini\esper\.agents\rules\esper-testing.md',
    r'C:\Users\KD\.gemini\esper\checklists\architecture.md',
    r'C:\Users\KD\.gemini\esper\checklists\automation-safety.md',
    r'C:\Users\KD\.gemini\esper\checklists\cleanup.md',
    r'C:\Users\KD\.gemini\esper\checklists\code-review.md',
    r'C:\Users\KD\.gemini\esper\checklists\orchestration.md',
    r'C:\Users\KD\.gemini\esper\checklists\documentation.md',
    r'C:\Users\KD\.gemini\esper\checklists\feature.md',
    r'C:\Users\KD\.gemini\esper\checklists\performance.md',
    r'C:\Users\KD\.gemini\esper\checklists\pull-request.md',
    r'C:\Users\KD\.gemini\esper\checklists\release.md',
    r'C:\Users\KD\.gemini\esper\checklists\security.md',
    r'C:\Users\KD\.gemini\esper\checklists\self-review.md',
    r'C:\Users\KD\.gemini\esper\checklists\testing.md',
    r'C:\Users\KD\.gemini\esper\principles\api-design.md',
    r'C:\Users\KD\.gemini\esper\principles\architecture.md',
    r'C:\Users\KD\.gemini\esper\principles\automation-safety.md',
    r'C:\Users\KD\.gemini\esper\principles\code-quality.md',
    r'C:\Users\KD\.gemini\esper\principles\communication.md',
    r'C:\Users\KD\.gemini\esper\principles\delegation.md',
    r'C:\Users\KD\.gemini\esper\principles\engineering.md',
    r'C:\Users\KD\.gemini\esper\principles\performance.md',
    r'C:\Users\KD\.gemini\esper\principles\reasoning.md',
    r'C:\Users\KD\.gemini\esper\principles\refactoring.md',
    r'C:\Users\KD\.gemini\esper\principles\reflection.md',
    r'C:\Users\KD\.gemini\esper\principles\retrieval.md',
    r'C:\Users\KD\.gemini\esper\principles\security.md',
    r'C:\Users\KD\.gemini\esper\principles\testing.md',
    r'C:\Users\KD\.gemini\esper\principles\reporting\findings.md',
    r'C:\Users\KD\.gemini\esper\principles\reporting\report-structure.md',
    r'C:\Users\KD\.gemini\esper\principles\reporting\rubric.md',
    r'C:\Users\KD\.gemini\esper\principles\reporting\taxonomy.md',
    r'C:\Users\KD\.gemini\esper\prompts\architecture-review.md',
    r'C:\Users\KD\.gemini\esper\prompts\bug-investigation.md',
    r'C:\Users\KD\.gemini\esper\prompts\code-review.md',
    r'C:\Users\KD\.gemini\esper\prompts\orchestration.md',
    r'C:\Users\KD\.gemini\esper\prompts\documentation.md',
    r'C:\Users\KD\.gemini\esper\prompts\explain.md',
    r'C:\Users\KD\.gemini\esper\prompts\feature.md',
    r'C:\Users\KD\.gemini\esper\prompts\performance-review.md',
    r'C:\Users\KD\.gemini\esper\prompts\refactor.md',
    r'C:\Users\KD\.gemini\esper\prompts\research.md',
    r'C:\Users\KD\.gemini\esper\prompts\retrospective.md',
    r'C:\Users\KD\.gemini\esper\prompts\security-review.md',
    r'C:\Users\KD\.gemini\esper\prompts\testing.md',
    r'C:\Users\KD\.gemini\esper\templates\architecture-review.md',
    r'C:\Users\KD\.gemini\esper\templates\audit-report.md',
    r'C:\Users\KD\.gemini\esper\templates\bug-investigation.md',
    r'C:\Users\KD\.gemini\esper\templates\code-review.md',
    r'C:\Users\KD\.gemini\esper\templates\design-doc.md',
    r'C:\Users\KD\.gemini\esper\templates\documentation-review.md',
    r'C:\Users\KD\.gemini\esper\templates\explain.md',
    r'C:\Users\KD\.gemini\esper\templates\implementation-plan.md',
    r'C:\Users\KD\.gemini\esper\templates\performance-analysis.md',
    r'C:\Users\KD\.gemini\esper\templates\research-report.md',
    r'C:\Users\KD\.gemini\esper\templates\security-review.md',
    r'C:\Users\KD\.gemini\esper\templates\shared-scratchpad.md',
    r'C:\Users\KD\.gemini\esper\templates\synthesis.md',
    r'C:\Users\KD\.gemini\esper\workflows\agent-communication.md',
    r'C:\Users\KD\.gemini\esper\workflows\architecture-review.md',
    r'C:\Users\KD\.gemini\esper\workflows\code-review.md',
    r'C:\Users\KD\.gemini\esper\workflows\code-writing.md',
    r'C:\Users\KD\.gemini\esper\workflows\debugging.md',
    r'C:\Users\KD\.gemini\esper\workflows\orchestration.md',
    r'C:\Users\KD\.gemini\esper\workflows\documentation.md',
    r'C:\Users\KD\.gemini\esper\workflows\explain.md',
    r'C:\Users\KD\.gemini\esper\workflows\performance-review.md',
    r'C:\Users\KD\.gemini\esper\workflows\refactor.md',
    r'C:\Users\KD\.gemini\esper\workflows\research.md',
    r'C:\Users\KD\.gemini\esper\workflows\revision.md',
    r'C:\Users\KD\.gemini\esper\workflows\security-review.md',
    r'C:\Users\KD\.gemini\esper\workflows\testing.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-ask\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-audit\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-clarify\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-cpt\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-doc\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-edit\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-hunt\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-meta-context\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-note\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-orch\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-plan\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-rag\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-repair\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-repo-map\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-report\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-retro\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-safety-gate\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-scaffold\SKILL.md',
    r'C:\Users\KD\.gemini\config\skills\esper-skills\esp-update-changelog\SKILL.md',
]

def process_content(content, path):
    # Determine the type based on the path
    type_str = ''
    if 'checklists' in path: type_str = 'checklist'
    elif 'principles' in path: type_str = 'principle'
    elif 'prompts' in path: type_str = 'prompt'
    elif 'templates' in path: type_str = 'template'
    elif 'workflows' in path: type_str = 'workflow'
    elif 'esper-skills' in path: type_str = 'skill'
    elif '.agents' in path: type_str = 'rule'
    else: type_str = 'module'
    
    # Extract the previous root tag if present
    match = re.search(r'<esper_([a-z_]+)>', content)
    if match:
        type_str = match.group(1)
        if type_str == 'principles': type_str = 'principle'
    
    # 1. Replace the root tags
    content = re.sub(r'<esper_[a-z_]+>', f'<esper_module type=\"{type_str}\">', content)
    content = re.sub(r'</esper_[a-z_]+>', f'</esper_module>', content)
    
    # 2. Bespoke tags -> <instructions>
    # Find all bespoke bodies that should be instructions
    for tag in ['security_verification', 'implementation_verification', 'protocol', 'workflow', 'principles']:
        if f'<{tag}>' in content or f'<{tag} ' in content:
            # We want to replace <tag> with <instructions>
            content = re.sub(fr'<{tag}([^>]*)>', r'<instructions\1>', content)
            content = re.sub(fr'</{tag}>', r'</instructions>', content)

    # For <protocol> with plain text numbers (like in checklists/cleanup.md)
    # They should be converted to <step> elements. But let's first check if there are raw numbers
    def replace_numbered_list(m):
        inner = m.group(1)
        inner = re.sub(r'(?m)^(\s*)\d+\.\s+(.*)$', r'\1<step>\2</step>', inner)
        if '<step>' in inner and '<execution_steps>' not in inner:
            inner = f'\n<execution_steps>\n{inner.strip()}\n</execution_steps>\n'
        return f'<instructions>{inner}</instructions>'
    
    if '<instructions>' in content and '</instructions>' in content:
        # Just run the numbered list replacement on the whole instructions block
        content = re.sub(r'<instructions>(.*?)</instructions>', replace_numbered_list, content, flags=re.DOTALL)
        
    # Fix hardcoded numbering inside <step> tags
    content = re.sub(r'<step>\s*\d+\.\s*(.*?)</step>', r'<step>\1</step>', content)

    # 3. Consolidate dependencies
    # <required_dependencies> -> <required>
    content = content.replace('<required_dependencies>', '<required>')
    content = content.replace('</required_dependencies>', '</required>')
    
    # <optional_dependencies> -> <optional>
    content = content.replace('<optional_dependencies>', '<optional>')
    content = content.replace('</optional_dependencies>', '</optional>')
    
    # Group them under <dependencies>
    deps_pattern = re.compile(r'(<required>.*?</required>\s*|<optional>.*?</optional>\s*|<canonical_sources>.*?</canonical_sources>\s*)+', re.DOTALL)
    
    def group_deps(m):
        inner = m.group(0).strip()
        return f'<dependencies>\n{inner}\n</dependencies>\n'
        
    content = deps_pattern.sub(group_deps, content)
    
    # Avoid nested <dependencies> if multiple matches were grouped
    # This simple regex approach might wrap them multiple times if they were separated.
    # A safer way is to just wrap the whole chunk if it's contiguous.
    
    return content

for file_path in files:
    if not os.path.exists(file_path): continue
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = process_content(content, file_path)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
