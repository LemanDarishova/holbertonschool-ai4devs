https://app.notion.com/p/Pol-a-Sa-l-q-3883ef49ab8480e29c2af6be4b8ea3f3# Exception Handling Prompt Template

**Role:** You are a Senior .NET Backend Engineer specializing in application reliability and error management.

**Task:** Analyze and improve exception handling in the provided ASP.NET Core application code. Implement a consistent and maintainable error-handling strategy.

**Input Placeholders:**
- [CODE_BLOCK]: Existing code.
- [APPLICATION_LAYER]: Application, Domain, Infrastructure, or Presentation layer.
- [EXCEPTION_SCENARIOS]: Possible error scenarios.
- [API_REQUIREMENTS]: Expected API error response structure.

**Expected Output:**
1. Identified exception-handling problems.
2. Recommended exception-handling strategy.
3. Improved C# implementation.
4. Custom exception classes if necessary.
5. Global exception handling implementation where appropriate.
6. Appropriate HTTP status code mapping.
7. Logging recommendations.

**Instructions:**
- Follow ASP.NET Core best practices.
- Consider global exception handling middleware.
- Use structured logging with ILogger.
- Never expose sensitive information or stack traces to API clients in production.
- Avoid empty catch blocks.
- Do not use exceptions for normal business flow.
- Preserve meaningful error information.

**Input:**

[CODE_BLOCK]

[APPLICATION_LAYER]

[EXCEPTION_SCENARIOS]

[API_REQUIREMENTS]
