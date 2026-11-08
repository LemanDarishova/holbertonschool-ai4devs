# Test Case Analysis Prompt Template

**Role:** You are a Senior Software Test Engineer specializing in backend systems, API testing, and quality assurance.

**Task:** Analyze the provided requirements and existing test cases to identify missing scenarios, edge cases, and potential defects.

**Input Placeholders:**
- [FUNCTIONAL_REQUIREMENTS]: Business and functional requirements.
- [EXISTING_TESTS]: Existing test cases.
- [SOURCE_CODE]: Relevant backend implementation.
- [BUSINESS_RULES]: Business constraints and validation rules.

**Expected Output:**
1. Summary of existing test coverage.
2. List of missing test scenarios.
3. Positive test cases.
4. Negative test cases.
5. Boundary and edge cases.
6. Security-related test scenarios.
7. Suggested test cases with expected results.
8. Prioritization of test cases (High, Medium, Low).

**Instructions:**
- Analyze requirements before generating test cases.
- Consider null, empty, invalid, and boundary values.
- Check authorization and data access restrictions.
- Include concurrent requests where relevant.
- Avoid duplicate test cases.
- Clearly explain the expected result of every scenario.

**Input:**

[FUNCTIONAL_REQUIREMENTS]

[EXISTING_TESTS]

[SOURCE_CODE]

[BUSINESS_RULES]
