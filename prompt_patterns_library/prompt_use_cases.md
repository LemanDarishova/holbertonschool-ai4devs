**Prompt Use Cases

This document identifies common use cases where reusable AI prompt patterns can improve productivity, code quality, and reliability in software development workflows.

1. Code Quality

- **Code Refactoring**
  - **Goal:** Improve code readability, maintainability, and performance without changing its existing behavior.
  - **Input:** Source code written in [LANGUAGE], including relevant classes, methods, and dependencies.
  - **Output:** Refactored code following clean code principles, along with an explanation of the improvements.

- **Code Review**
  - **Goal:** Identify potential bugs, code smells, security issues, and violations of coding standards.
  - **Input:** Source code, project requirements, and coding conventions.
  - **Output:** A structured code review report containing identified issues, their severity, and suggested solutions.

- **Design Pattern Implementation**
  - **Goal:** Apply appropriate software design patterns to improve code organization and maintainability.
  - **Input:** Existing code, project architecture, and functional requirements.
  - **Output:** Improved code using suitable design patterns, with explanations of why they were selected.

## 2. Debugging

- **Bug Identification**
  - **Goal:** Identify the root cause of unexpected application behavior.
  - **Input:** Source code, error messages, stack traces, and steps to reproduce the issue.
  - **Output:** Explanation of the root cause and a corrected version of the code.

- **Exception Handling**
  - **Goal:** Improve exception handling and prevent unexpected application crashes.
  - **Input:** Code containing potential runtime exceptions and relevant application requirements.
  - **Output:** Improved exception handling implementation with appropriate error messages and logging recommendations.

- **API Error Debugging**
  - **Goal:** Identify and resolve errors occurring in REST API endpoints.
  - **Input:** API endpoint code, HTTP request and response details, status codes, and error logs.
  - **Output:** Identified API issues, corrected implementation, and recommendations for proper HTTP status code handling.

## 3. Documentation

- **API Documentation Generation**
  - **Goal:** Generate clear and structured documentation for REST API endpoints.
  - **Input:** Controller classes, endpoint definitions, request DTOs, response models, and authentication requirements.
  - **Output:** API documentation describing HTTP methods, endpoints, parameters, request bodies, response formats, and possible status codes.

- **Code Documentation**
  - **Goal:** Make complex code easier to understand and maintain.
  - **Input:** Source code containing classes, methods, and business logic.
  - **Output:** Meaningful code comments, XML documentation, and explanations of important methods and classes.

- **README File Generation**
  - **Goal:** Create comprehensive documentation for setting up and using a software project.
  - **Input:** Project structure, technologies, dependencies, configuration requirements, and execution instructions.
  - **Output:** A structured README.md file containing project overview, installation steps, configuration, usage instructions, and examples.

## 4. Testing

- **Unit Test Generation**
  - **Goal:** Improve code reliability by generating unit tests for individual methods and services.
  - **Input:** Source code, method descriptions, expected behavior, and testing framework [e.g., xUnit, NUnit, or MSTest].
  - **Output:** Unit tests covering normal scenarios, edge cases, and expected exceptions.

- **Integration Test Generation**
  - **Goal:** Verify that different application components work correctly together.
  - **Input:** API endpoints, service dependencies, database configuration, and application requirements.
  - **Output:** Integration tests covering HTTP requests, database interactions, and component communication.

- **Test Case Analysis**
  - **Goal:** Identify missing test scenarios and improve test coverage.
  - **Input:** Existing test cases, source code, and functional requirements.
  - **Output:** A list of missing test scenarios, edge cases, and additional test cases with expected results.

## 5. Code Generation

- **CRUD API Generation**
  - **Goal:** Generate standard Create, Read, Update, and Delete operations for a given entity.
  - **Input:** Entity definition, database structure, technology stack, and API requirements.
  - **Output:** Complete CRUD implementation including controllers, services, repositories, DTOs, and validation where appropriate.

- **Database Query Generation**
  - **Goal:** Generate efficient database queries based on application requirements.
  - **Input:** Database schema, entity relationships, and required data retrieval conditions.
  - **Output:** Optimized SQL or Entity Framework Core LINQ queries with explanations of their logic and performance considerations.

- **Input Validation Generation**
  - **Goal:** Ensure that incoming API requests contain valid and consistent data.
  - **Input:** Request DTOs, field requirements, validation rules, and business constraints.
  - **Output:** Validation implementation using [VALIDATION_FRAMEWORK], including appropriate error messages and validation rules.
