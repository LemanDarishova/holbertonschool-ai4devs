# CRUD REST API Generation Prompt Template

**Role:** You are a Senior C# Backend Developer specializing in ASP.NET Core, Entity Framework Core, REST APIs, and Clean Architecture.

**Task:** Design and implement CRUD operations for the specified entity while following the existing project architecture and coding conventions.

**Input Placeholders:**
- [ENTITY_DEFINITION]: Entity properties and relationships.
- [PROJECT_ARCHITECTURE]: Clean Architecture, N-Tier, or another structure.
- [DATABASE_TYPE]: SQL Server, PostgreSQL, or another database.
- [API_REQUIREMENTS]: Required endpoints and business rules.
- [EXISTING_CODE]: Existing project implementation.
- [VALIDATION_RULES]: Input validation requirements.

**Expected Output:**
1. Entity and relationship analysis.
2. DTO definitions.
3. Repository and service implementation where required by the architecture.
4. CRUD API endpoints.
5. Entity Framework Core configuration.
6. Input validation.
7. Appropriate HTTP status codes.
8. Example API requests and responses.
9. Unit and integration testing recommendations.

**Instructions:**
- Follow SOLID and Clean Architecture principles.
- Use asynchronous database operations.
- Use DTOs instead of exposing database entities directly.
- Apply proper validation.
- Prevent over-posting and unauthorized data access.
- Follow existing project conventions.
- Do not introduce unnecessary layers or abstractions.
- Explain any architectural decisions.

**Input:**

[ENTITY_DEFINITION]

[PROJECT_ARCHITECTURE]

[DATABASE_TYPE]

[API_REQUIREMENTS]

[EXISTING_CODE]

[VALIDATION_RULES]
