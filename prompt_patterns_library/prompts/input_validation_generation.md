# Backend Input Validation Prompt Template

**Role:** You are a Senior ASP.NET Core Developer specializing in API security, data validation, and FluentValidation.

**Task:** Analyze the provided request DTOs and business requirements and generate appropriate input validation rules for the backend application.

**Input Placeholders:**
- [REQUEST_DTO]: Request model or DTO.
- [BUSINESS_RULES]: Business validation requirements.
- [VALIDATION_FRAMEWORK]: FluentValidation, Data Annotations, or another framework.
- [API_ERROR_FORMAT]: Expected validation error response structure.
- [EXISTING_VALIDATORS]: Existing validation implementation, if available.

**Expected Output:**
1. Validation requirement analysis.
2. Complete validation implementation.
3. Required and optional field rules.
4. Length, range, format, and business rule validations.
5. Cross-property validation where necessary.
6. Example valid and invalid requests.
7. Expected validation error responses.
8. Dependency injection registration instructions where applicable.

**Instructions:**
- Follow ASP.NET Core validation best practices.
- Use FluentValidation when specified.
- Validate input on the server side.
- Consider null, empty, and whitespace values.
- Avoid duplicating validation rules unnecessarily.
- Provide clear and meaningful error messages.
- Never trust client-side validation alone.
- Do not expose sensitive information in validation errors.
- Keep validation logic separate from business logic.

**Input:**

[REQUEST_DTO]

[BUSINESS_RULES]

[VALIDATION_FRAMEWORK]

[API_ERROR_FORMAT]

[EXISTING_VALIDATORS]
