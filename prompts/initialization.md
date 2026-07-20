---
name: Initialization
---

<esper_module type="prompt">
  <title>Initialization Prompt</title>
  <purpose>Trigger the initialization of Esper context for a new project.</purpose>
  <when_to_use>
    <item>initializing a new project</item>
    <item>setting up Esper context in a project that lacks it</item>
  </when_to_use>
  <instructions>
    <item>Execute the initialization workflow to bootstrap the `.esper/` directory.</item>
  </instructions>
  <dependencies>
    <required>
      <item>workflows/initialization.md</item>
    </required>
  </dependencies>
</esper_module>
