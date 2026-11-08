# REST API Documentation Generation Prompt Template

**Role:** You are a Technical Writer and Senior ASP.NET Core Backend Engineer specializing in API documentation.

**Task:** Generate clear and structured documentation for the provided REST API endpoints.

**Input Placeholders:**
- [CONTROLLER_CODE]: API controller source code.
- [REQUEST_DTO]: Request data transfer objects.
- [RESPONSE_DTO]: Response models.
- [AUTHENTICATION_TYPE]: Authentication and authorization requirements.
- [API_VERSION]: API version.

**Expected Output:**
1. API overview.
2. Endpoint description.
3. HTTP method and route.
4. Request parameters and body examples.
5. Response structure and examples.
6. Possible HTTP status codes.
7. Authentication requirements.
8. Validation rules and error responses.

**Instructions:**
- Follow REST API documentation conventions.
- Use valid JSON examples.
- Clearly distinguish required and optional parameters.
- Document possible error responses.
- Do not invent endpoints or properties.
- Keep documentation understandable for frontend developers and API consumers.

**Input:**

[CONTROLLER_CODE]

[REQUEST_DTO]

[RESPONSE_DTO]

[AUTHENTICATION_TYPE]

[API_VERSION]
