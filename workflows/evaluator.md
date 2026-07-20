---
name: Evaluator-Optimizer Middleware
---

<esper_module type="workflow">
<purpose>
Provides a strict validation and reflection loop for Agent-to-Agent (A2A) data contracts.
</purpose>
<when_to_use>
<item>Whenever an agent generates an A2A JSON payload</item>
<item>To ensure structural integrity before passing payloads down the execution graph</item>
</when_to_use>
<instructions>
<subsection>1. Generation and Validation</subsection>
When you generate an A2A JSON payload, you MUST save it to a file and run it through the Evaluator script:
`python C:/Users/KD/.gemini/esper/scripts/evaluator.py <path_to_json_file>`

<subsection>2. Reflection and Retry</subsection>
If the script outputs validation errors, you must reflect on the specific errors provided and attempt to fix the JSON payload.
When retrying, you MUST increment the `--retry-count` parameter. For example:
`python C:/Users/KD/.gemini/esper/scripts/evaluator.py <path_to_json_file> --retry-count 1`

<subsection>3. Failure and Hard-crash</subsection>
You have a maximum of 3 retries (i.e., `--retry-count 3`). If the JSON payload still fails validation at 3 retries, the Evaluator will exit with a non-zero code to hard-crash the workflow. You should stop execution and report the failure.
</instructions>
<dependencies>
<required>
<item>templates/a2a-contract.json</item>
</required>
</dependencies>
</esper_module>
