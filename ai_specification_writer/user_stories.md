BakuFlood AI — User Stories
User Story 1 — Flood Risk Map
As a resident, I want to see flood risks on a map so that I can avoid dangerous streets.

Acceptance Criteria:
- Each monitored location displays a low, medium, high, or unavailable risk level.
- Clicking a location shows its risk level and last update time.
Priority: MVP
User Story 2 — Sensor Data Collection
As an infrastructure operator, I want to collect IoT water-level readings so that I can monitor drainage conditions remotely.

Acceptance Criteria:
- Registered sensors can submit timestamped water-level readings.
- Valid readings are saved; invalid readings are rejected and logged.
Priority: MVP
User Story 3 — Weather Integration
As a risk analyst, I want to access rainfall data so that predictions reflect current weather conditions.

Acceptance Criteria:
- The system retrieves rainfall data from a configured weather provider.
- Weather records include source and timestamp; missing data is flagged.
Priority: MVP
User Story 4 — Flood Risk Prediction
As an infrastructure operator, I want to see calculated flood risks so that I can prioritize threatened locations.

Acceptance Criteria:
- Available sensor and weather data produce a low, medium, or high risk level.
- Each prediction stores location and time; insufficient data produces an unavailable status.
Priority: MVP
User Story 5 — Emergency Alerts
As an emergency officer, I want to receive high-risk alerts so that I can respond quickly.

Acceptance Criteria:
- A new high-risk event creates an alert with location and timestamp.
- The responsible authority is notified; duplicate alerts for the same active event are prevented.
Priority: MVP
User Story 6 — Alert Management
As a municipal officer, I want to manage active alerts so that I can track response progress.

Acceptance Criteria:
- The dashboard shows alert location, severity, time, and status.
- Authorized officers can acknowledge or resolve alerts; changes are logged.
Priority: MVP
User Story 7 — Personal Notifications
As a resident, I want to subscribe to area-based alerts so that I get warnings relevant to my location.

Acceptance Criteria:
- Users can opt in to warnings for selected monitored areas.
- High-risk events trigger notifications; unsubscribing stops future alerts.
Priority: High
User Story 8 — Sensor Health
As a system administrator, I want to check sensor health so that I can detect monitoring failures.

Acceptance Criteria:
- Sensors that exceed a configured reporting timeout are marked offline.
- Out-of-range readings are flagged, and the dashboard shows the last valid reading.
Priority: High
User Story 9 — Historical Analysis
As a city analyst, I want to review past flood data so that I can identify recurring problem areas.

Acceptance Criteria:
- Authorized users can filter historical readings and alerts by location and date.
- Results are chronological, and missing data is distinguished from low readings.
Priority: Medium
User Story 10 — Export Reports
As a municipal decision-maker, I want to download risk reports so that I can support infrastructure planning.

Acceptance Criteria:
- Users can select a location and time range for a report.
- The report includes risk observations and alert counts and is downloadable as CSV.
Priority: Medium
User Story 11 — Safer Routes
As a driver, I want to identify flood-risk sections of my route so that I can make safer travel decisions.

Acceptance Criteria:
- Users can enter a start and destination to display a suggested route.
- High-risk monitored route sections are highlighted; unmonitored roads are not labeled safe.
Priority: Medium
User Story 12 — Report Flooding
As a resident, I want to report flooding on a street so that authorities can investigate unmonitored areas.

Acceptance Criteria:
- Users can submit a location, time, and description of observed flooding.
- Reports are marked unverified until authorized staff review them.
Priority: Low
