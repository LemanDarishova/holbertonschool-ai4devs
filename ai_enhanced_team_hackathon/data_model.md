Data Model
Product: AI-Powered Urban Issue Reporter
The MVP uses a relational database. The main entities are User, IssueReport, and AIAnalysis. An issue report belongs to a user, and an issue can have an AI analysis.
Entities
1. User
Stores resident and administrator account information.
Field	Type	Description
UserId	UUID / Integer	Primary key
FullName	String	User's full name
Email	String	Unique email address
PasswordHash	String	Hashed password
Role	String / Enum	Resident or Administrator
CreatedAt	DateTime	Account creation date


2. IssueReport
Stores the urban issue submitted by a resident.
Field	Type	Description
IssueId	UUID / Integer	Primary key
UserId	UUID / Integer	Foreign key to User
Description	Text	User's description of the issue
Category	String / Enum	Road damage, streetlight, waste, water leakage, or other
Address	String	Human-readable location
Latitude	Decimal	Geographic latitude
Longitude	Decimal	Geographic longitude
PhotoUrl	String, nullable	Optional uploaded photo location
Priority	String / Enum	Low, Medium, or High
Status	String / Enum	Submitted, In Review, or Resolved
CreatedAt	DateTime	Report submission date
UpdatedAt	DateTime	Last update date


3. AIAnalysis
Stores the AI-generated analysis for an issue report.
Field	Type	Description
AnalysisId	UUID / Integer	Primary key
IssueId	UUID / Integer	Foreign key to IssueReport
SuggestedCategory	String	AI-suggested issue category
SuggestedPriority	String / Enum	AI-suggested priority
Summary	Text	Short AI-generated report summary
ConfidenceScore	Decimal, nullable	Optional confidence value if supported by the AI service
ReviewedByUserId	UUID / Integer, nullable	Administrator who reviewed the analysis
IsReviewed	Boolean	Whether an administrator reviewed it
CreatedAt	DateTime	Analysis creation date


Relationships
- One User can submit many IssueReports (1-to-many).
- One IssueReport can have one or more AIAnalysis records over time (1-to-many), allowing re-analysis if needed.
- One User acting as an administrator can review many AIAnalysis records (1-to-many, optional relationship).
Notes
- IssueReport.Category and IssueReport.Priority store the final values confirmed by an administrator or application workflow.
- AIAnalysis.SuggestedCategory and AIAnalysis.SuggestedPriority preserve the AI suggestions separately.
- Passwords must never be stored as plain text.
- Latitude and longitude should be validated before saving a report.
