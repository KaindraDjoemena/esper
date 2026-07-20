---
name: Memory Management
---

<esper_module type="workflow">
<purpose>
Manage token usage and prevent context bloat by executing deterministic sliding window and selective forgetting logic on shared context files.
</purpose>
<when_to_use>
<item>when generating or reading large amounts of context</item>
<item>during periodic maintenance of project context</item>
<item>when token limits are approaching</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Check if the `.esper/shared_context/` directory has grown too large or contains stale context.</step>
<step>Execute `python C:/Users/KD/.gemini/esper/scripts/memory_manager.py --prune` to clear stale memory.</step>
<step>Adjust the sliding window size by passing `--window-size <size>` if needed for the current task.</step>
<step>Document any crucial context that was pruned and may need to be summarized into a persistent memory file.</step>
</execution_steps>
</instructions>
<dependencies>
<required>
</required>
</dependencies>
</esper_module>
