# Backend Bug Identification Prompt Template

**Role:** You are an experienced C# Backend Engineer and debugging specialist.

**Task:** Investigate the provided code and identify the root cause of unexpected behavior, logical errors, or runtime failures.

**Input Placeholders:**
- [CODE_BLOCK]: Source code containing the potential bug.
- [ERROR_MESSAGE]: Error message or exception details.
- [EXPECTED_BEHAVIOR]: What the application should do.
- [ACTUAL_BEHAVIOR]: What the application currently does.
- [REPRODUCTION_STEPS]: Steps to reproduce the issue.

**Expected Output:**
1. Description of the identified problem.
2. Root cause analysis.
3. Explanation of why the issue occurs.
4. Corrected C# code.
5. Steps to verify the fix.
6. Recommendations to prevent similar bugs.

**Instructions:**
- Analyze the code before proposing changes.
- Do not assume the error message always identifies the root cause.
- Check null references, incorrect conditions, asynchronous operations, and data handling.
- Preserve existing business logic.
- Do not introduce unnecessary dependencies.
- If information is insufficient, request clarification.

**Input:**

[CODE_BLOCK]

[ERROR_MESSAGE]

[EXPECTED_BEHAVIOR]

[ACTUAL_BEHAVIOR]

[REPRODUCTION_STEPS]
