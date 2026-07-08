# Esper Benchmarking Suite (Epic 5)

## Overview
This directory contains the custom benchmarking orchestrator designed to rigorously evaluate the Esper Engineering Operating System. 

Unlike traditional LLM evaluations that rely purely on text-in/text-out, this suite provides **SWE-bench style sandboxing**. It gives the Esper agent a pristine, isolated Docker container to execute multi-step workflows, clone repositories, edit files, and run tests safely. 

This enables us to objectively measure **Functional Correctness** (e.g., did the bug fix actually pass `pytest`?) without risking your host machine or burning excessive LLM judge tokens.

---

## Architecture

*   **`orchestrator.py`**: The core Python engine. It reads the test configurations, dynamically builds the sandbox image, spins up containers for each test, executes Esper, and extracts the deterministic pass/fail results.
*   **`schema.yaml`**: The master configuration file where benchmark tests are defined.
*   **`Dockerfile.eval`**: The blueprint for the pristine sandbox environment. It ensures every test runs in a clean matrix with all necessary dependencies installed.
*   **`requirements.txt`**: The Python packages required to run the orchestrator (e.g., `docker-py`).

---

## How to Run the Benchmarks

### 1. Prerequisites
You must have Docker Desktop installed and running on your host machine.

### 2. Setup
Install the required Python dependencies for the orchestrator:
```bash
cd benchmarks/
pip install -r requirements.txt
```

### 3. Execution
Simply run the orchestrator script:
```bash
python orchestrator.py
```
The script will automatically:
1. Build the `esper-sandbox:latest` Docker image.
2. Iterate through every test defined in `schema.yaml`.
3. Spin up an isolated container, run the verification commands, and report `✅ PASSED` or `❌ FAILED`.
4. Delete the container immediately after the test completes.

---

## How to Add New Benchmarks

To add a new test case, simply append it to the `test_cases` array in `schema.yaml`. 

**Example Schema:**
```yaml
  - id: "my_custom_benchmark"
    description: "Fix a specific bug in a target repo"
    repository: "https://github.com/my-org/my-repo"
    commit_hash: "a1b2c3d4" # The exact state of the code you want to test
    esper_prompt: "Fix the bug in the authentication logic."
    verification:
      command: "pytest tests/test_auth.py" # The deterministic check
      expected_exit_code: 0
      timeout_seconds: 60
```

---

## Next Steps / Roadmap
- **Agent Injection:** Update `orchestrator.py` to seamlessly mount or copy your specific CLI harness into the `Dockerfile.eval` so it can be invoked via the orchestrator.
- **Observability:** Integrate LangSmith SDK to trace token usage and tool calls during execution.
- **Opus Judge:** Hook up an LLM-as-a-judge pipeline for qualitative tasks (like grading architectural reports against Esper's canonical rubric).
