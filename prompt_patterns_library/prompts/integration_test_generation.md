# Integration Test Generation Prompt Template

**Role:** You are a Senior .NET QA Engineer specializing in ASP.NET Core integration testing and API reliability.

**Task:** Generate integration tests to verify that application components work correctly together, including API endpoints, dependency injection, middleware, and database interactions.

**Input Placeholders:**
- [APPLICATION_CODE]: Application implementation.
- [API_ENDPOINTS]: Endpoints to test.
- [DATABASE_TYPE]: SQL Server, PostgreSQL, or other database.
- [TEST_ENVIRONMENT]: Test environment configuration.
- [EXPECTED_BEHAVIOR]: Expected application behavior.
- [TEST_FRAMEWORK]: xUnit, NUnit, or MSTest.

**Expected Output:**
1. Integration testing strategy.
2. Required test configuration.
3. WebApplicationFactory setup where appropriate.
4. Database test setup and cleanup.
5. Complete integration test classes.
6. HTTP request and response assertions.
7. Instructions for executing tests.

**Instructions:**
- Test real application behavior rather than isolated methods.
- Use appropriate test database isolation.
- Avoid modifying production data.
- Verify HTTP status codes and response bodies.
- Test authentication and authorization where relevant.
- Ensure tests are repeatable and independent.
- Keep test configuration separate from production configuration.

**Input:**

[APPLICATION_CODE]

[API_ENDPOINTS]

[DATABASE_TYPE]

[TEST_ENVIRONMENT]

[EXPECTED_BEHAVIOR]

[TEST_FRAMEWORK]
