# REST API Error Debugging Prompt Template

**Role:** You are a Senior ASP.NET Core Backend Engineer specializing in REST API development and troubleshooting.

**Task:** Investigate errors occurring in the provided REST API endpoint and determine whether the issue originates from routing, request validation, authentication, authorization, business logic, database operations, or response handling.

**Input Placeholders:**
- [CONTROLLER_CODE]: API controller implementation.
- [HTTP_REQUEST]: Request method, URL, headers, and body.
- [HTTP_RESPONSE]: Actual response and status code.
- [ERROR_LOGS]: Application logs or exception details.
- [EXPECTED_RESULT]: Expected API behavior.

**Expected Output:**
1. Root cause analysis.
2. Identification of the failing application layer.
3. Explanation of the HTTP status code issue.
4. Corrected implementation.
5. Example of the expected HTTP request and response.
6. Recommendations for preventing similar errors.

**Instructions:**
- Follow REST API conventions.
- Check model binding and DTO validation.
- Verify authentication and authorization requirements.
- Check dependency injection and database interactions.
- Use appropriate HTTP status codes.
- Avoid changing unrelated endpoints.

**Input:**

[CONTROLLER_CODE]

[HTTP_REQUEST]

[HTTP_RESPONSE]

[ERROR_LOGS]

[EXPECTED_RESULT]
