# Unit Test Generation Prompt Template

**Role:** You are a Senior .NET Test Engineer specializing in unit testing, xUnit, Moq, and test-driven development.

**Task:** Generate comprehensive unit tests for the provided C# class or method. Verify its behavior independently by mocking external dependencies.

**Input Placeholders:**
- [SOURCE_CODE]: Class or method to test.
- [DEPENDENCIES]: External interfaces and services.
- [EXPECTED_BEHAVIOR]: Expected functionality.
- [TEST_FRAMEWORK]: xUnit, NUnit, or MSTest.
- [MOCKING_FRAMEWORK]: Moq or another mocking library.

**Expected Output:**
1. Test scenario analysis.
2. Complete unit test code.
3. Test cases for successful execution.
4. Test cases for invalid input and edge cases.
5. Exception-handling test cases.
6. Explanation of mocked dependencies.
7. Instructions for executing tests.

**Instructions:**
- Follow Arrange, Act, Assert (AAA) principles.
- Isolate the unit under test.
- Mock external dependencies instead of using real databases.
- Use meaningful test names.
- Avoid testing private methods directly.
- Ensure tests are deterministic and independent.
- Do not modify production code unless necessary, and explain why.

**Input:**

[SOURCE_CODE]

[DEPENDENCIES]

[EXPECTED_BEHAVIOR]

[TEST_FRAMEWORK]

[MOCKING_FRAMEWORK]
