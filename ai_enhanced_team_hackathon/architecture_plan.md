Architecture Plan
Product: AI-Powered Urban Issue Reporter
1. Overview
The application will use a simple client-server architecture. Residents submit urban issue reports through a web interface. The backend validates and stores the reports, sends relevant information to an AI service for analysis, and returns the results. Administrators use a dashboard to review reports, correct AI suggestions, and update report statuses.
2. High-Level Architecture
                 +---------------------------+
                 |       Web Frontend        |
                 | Resident UI / Admin UI    |
                 +-------------+-------------+
                               |
                         HTTPS / REST API
                               |
                 +-------------v-------------+
                 |       Backend API         |
                 | Authentication            |
                 | Report Management         |
                 | Validation & Authorization|
                 +------+---------------+----+
                        |               |
                  Read / Write       AI request
                        |               |
              +---------v----+   +------v-----------+
              | Relational   |   | AI Service       |
              | Database     |   | Classification   |
              | Users        |   | Priority estimate|
              | IssueReports |   | Summary generation|
              | AIAnalysis   |   +------------------+
              +--------------+
                        |
                 +------v------+
                 | File Storage|
                 | Issue photos|
                 +-------------+
3. Main Components
Frontend
- Provides a report submission form for residents.
- Allows users to enter a description, location, and optional photo.
- Displays submitted reports and their statuses.
- Provides an administrator dashboard with search, filters, report details, and status controls.
Backend API
- Handles registration, login, and role-based access.
- Validates report descriptions, locations, and uploaded files.
- Creates and retrieves issue reports.
- Calls the AI service and stores its analysis.
- Allows authorized administrators to review AI suggestions and update report status.
- Exposes REST API endpoints to the frontend.
Relational Database
- Stores users, issue reports, and AI analysis results.
- Enforces relationships using primary and foreign keys.
- Stores final report values separately from AI suggestions.
AI Service
- Receives the issue description and relevant report information.
- Suggests a category and priority level.
- Generates a concise summary for administrators.
- Returns structured output that the backend validates before saving.
- Provides decision support only; administrators can review and change suggestions.
File Storage
- Stores optional photos uploaded with issue reports.
- The database stores the photo URL or storage key rather than the image binary itself.
4. Main Data Flow
1. A resident signs in and submits an issue description, location, and optional photo.
2. The frontend sends the report to the backend through a REST API.
3. The backend validates the input and saves the report with the status Submitted.
4. The backend sends the report description to the AI service.
5. The AI service returns a suggested category, priority, and short summary.
6. The backend validates and stores the AI result in AIAnalysis.
7. The administrator reviews the report and AI suggestions, then confirms or edits the category and priority.
8. The administrator updates the report status. The resident can view the latest status in the application.
5. Suggested Technology Stack
Layer	Suggested Technology
Frontend	React
Backend	ASP.NET Core Web API
Database	PostgreSQL
AI Integration	Hosted LLM API (provider to be selected)
Photo Storage	Local storage for development; cloud object storage for deployment
API Format	REST / JSON
Authentication	ASP.NET Core Identity or JWT-based authentication


The technologies are suggestions for the MVP and can be adjusted based on team experience and available services.
6. Security and Reliability Considerations
- Use HTTPS for communication between the frontend and backend.
- Hash passwords and never store plain-text credentials.
- Apply role-based authorization to administrator operations.
- Validate and restrict uploaded photo file types and sizes.
- Do not send personal account information to the AI service unless it is necessary.
- Treat AI output as a suggestion, validate its structure, and allow administrator review.
- Handle AI service timeouts or failures gracefully; the report should still be saved even if AI analysis is temporarily unavailable.
7. MVP Implementation Order
1. Create the database schema and backend project.
2. Implement authentication and resident report submission.
3. Implement report listing, details, and status management.
4. Integrate AI classification, priority estimation, and summary generation.
5. Build the resident pages and administrator dashboard.
6. Test the main user flows, authorization rules, and AI failure handling.
