BakuFlood AI — User Stories
Overview
These user stories describe the main capabilities of BakuFlood AI, an IoT- and AI-assisted flood monitoring and early warning system for Baku. Acceptance criteria define verifiable behavior for an initial product implementation.

Priority definitions: MVP = essential for the first usable release; High = important next capability; Medium = valuable enhancement; Low = optional later improvement.
User Story 1 — View Flood Risks on a Map
As a Baku resident, I want to view flood risk levels for monitored streets on an interactive map so that I can avoid potentially dangerous areas.

Acceptance Criteria:
- The map displays every configured monitoring location with a low, medium, high, or unavailable risk status.
- Selecting a location shows its risk level and the timestamp of the latest update.
- Locations with missing or outdated data are marked as unavailable rather than shown as safe.
Priority: MVP
User Story 2 — Collect Water-Level Sensor Data
As a municipal infrastructure operator, I want to receive measurements from installed IoT water-level sensors so that I can monitor changing water conditions without visiting every site.

Acceptance Criteria:
- The system accepts a reading only if it identifies a registered sensor and includes a timestamp and water-level value.
- Valid readings are stored and associated with the correct monitoring location.
- Invalid readings are rejected and recorded for troubleshooting without changing the displayed water level.
Priority: MVP
User Story 3 — Integrate Weather Information
As a flood risk analyst, I want to combine sensor data with rainfall observations and forecasts so that risk assessments account for changing weather conditions.

Acceptance Criteria:
- The system retrieves rainfall data from at least one configured meteorological provider.
- Each weather record includes its source, observation or forecast time, and the area it covers.
- If weather data is unavailable, the system flags the missing input instead of treating rainfall as zero.
Priority: MVP
User Story 4 — Calculate Area-Specific Flood Risk
As a municipal infrastructure operator, I want to receive calculated flood risk levels for monitored areas so that I can identify where intervention may be needed.

Acceptance Criteria:
- The risk assessment service uses available sensor and weather inputs to assign a low, medium, or high risk level to each eligible monitoring area.
- Every calculated risk record stores its location, assessment timestamp, and the data or model version used.
- When required inputs are insufficient, the service returns an unavailable status and does not present a confident risk classification.
Priority: MVP
User Story 5 — Receive High-Risk Alerts
As an emergency response officer, I want to receive alerts when an area reaches a high flood risk level so that I can coordinate a timely response.

Acceptance Criteria:
- A new high-risk event automatically creates an alert containing the location, risk level, and event time.
- The system sends the alert to the configured responsible authority through at least one operational notification channel.
- Repeated assessments of the same ongoing event do not generate duplicate new-event alerts.
Priority: MVP
User Story 6 — Manage and Monitor Active Alerts
As a municipal operations officer, I want to view and update active flood alerts in a dashboard so that I can coordinate and track responses.

Acceptance Criteria:
- The dashboard lists active alerts with location, severity, creation time, and current status.
- An authorized officer can change an alert status to acknowledged or resolved.
- Each status change is saved with a timestamp and the identity of the officer who made it.
Priority: MVP
User Story 7 — Subscribe to Location-Based Notifications
As a resident, I want to subscribe to flood warnings for selected areas so that I receive relevant alerts without constantly checking the map.

Acceptance Criteria:
- A user can select one or more monitored areas and explicitly opt in to notifications.
- A high-risk event in a subscribed area triggers a notification containing the affected location and warning time.
- A user can unsubscribe, after which no new subscription-based notifications are sent for that area.
Priority: High
User Story 8 — Monitor Sensor Health
As a system administrator, I want to identify sensors that stop reporting or send abnormal values so that maintenance teams can restore reliable monitoring.

Acceptance Criteria:
- A sensor is flagged as offline if it has not reported within its configured reporting timeout.
- Readings outside a sensor's configured valid range are flagged and excluded from normal risk calculations.
- The dashboard shows the sensor's health status and the time of its most recent valid reading.
Priority: High
User Story 9 — Review Flood History
As a city planning analyst, I want to review historical water levels, risk estimates, and alerts so that I can identify recurring flood hotspots.

Acceptance Criteria:
- An authorized analyst can filter historical records by monitored location and date range.
- The results show recorded water levels, risk classifications, and alerts in chronological order.
- A period with no observations is clearly distinguished from a period with measured low water levels.
Priority: Medium
User Story 10 — Export Risk Reports
As a municipal decision-maker, I want to export flood monitoring reports so that I can share evidence when planning infrastructure improvements.

Acceptance Criteria:
- An authorized user can select an area and date range for a report.
- The report contains the selected period, number of alerts, and a summary of available risk observations.
- The report can be downloaded in CSV format with readable column headers.
Priority: Medium
User Story 11 — Find Safer Routes
As a driver, I want to see which parts of my planned route intersect high-risk monitored streets so that I can decide whether to change my journey.

Acceptance Criteria:
- A user can enter a starting point and destination and view the suggested route on the map.
- Route segments intersecting a currently high-risk monitored area are visibly highlighted.
- The interface explains that risk coverage is limited to monitored areas and does not guarantee that unmarked streets are flood-free.
Priority: Medium
User Story 12 — Submit a Flood Observation
As a Baku resident, I want to report visible street flooding so that responsible teams can investigate locations that may not have sensors.


Notes
- Exact risk thresholds, sensor timeouts, notification delivery targets, and prediction accuracy requirements must be defined during technical specification and pilot testing.
- Alerts are decision-support information and should not be presented as guarantees of safety.
