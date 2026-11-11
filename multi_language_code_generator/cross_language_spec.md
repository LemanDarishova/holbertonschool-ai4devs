Cross-Language Specification — Urban Flood Risk Analyzer
1. Algorithm Description
Project: BakuFlood AI
Algorithm: Urban Flood Risk Analyzer
Goal: Estimate flood risk for a monitored street using rainfall, measured water depth, and drainage condition. The same deterministic rules must produce identical outputs in Python, JavaScript, or any other implementation language.

For every observation, calculate three risk contributions and add them:
Rainfall score
Rainfall (mm)	Points
0 to less than 15	0
15 to less than 30	15
30 to less than 50	30
50 or more	45


Water-level score
Water depth (cm)	Points
0 to less than 10	0
10 to less than 25	20
25 to less than 50	40
50 or more	60


Drainage-condition score
Condition	Points
good	0
partial	10
blocked	25


Compute:

score = min(100, rainfall_points + water_points + drainage_points)

Assign the classification:
- Low: score from 0 to 29 inclusive.
- Medium: score from 30 to 59 inclusive.
- High: score from 60 to 100 inclusive.
These thresholds are illustrative software-testing rules, not scientifically validated flood warnings. Real deployment requires local calibration, expert review, and field validation.
2. Input Format
The algorithm accepts one JSON object per evaluation:
{
  "location_id": "BAKU-001",
  "rainfall_mm": 35,
  "water_level_cm": 28,
  "drainage_status": "partial"
}
Required fields:
Field	Type	Constraint
location_id	string	Nonempty after trimming whitespace
rainfall_mm	number	Finite, nonnegative; not a Boolean
water_level_cm	number	Finite, nonnegative; not a Boolean
drainage_status	string	Exactly good, partial, or blocked (case-sensitive)


Decimal numeric values are allowed. Numeric strings, missing fields, null, infinity, and NaN are invalid. No unit conversions are performed.
3. Output Format
For valid input, return exactly this JSON structure with the original location ID, integer score, and classification:
{
  "location_id": "BAKU-001",
  "risk_score": 80,
  "risk_level": "High"
}
For any invalid input, return exactly:
{
  "error": "Invalid input"
}
Errors do not produce a score or risk classification. JSON object key order is not significant.
4. Edge Cases
1. Zero rainfall and water depth: Both receive zero points; drainage can still add risk points.
2. Exact thresholds: Values equal to a threshold belong to the higher bracket (for example, 15 mm gives 15 points).
3. Very large measurements: The total score is capped at 100.
4. Missing or invalid measurements: Return the error object, never guess a risk level.
5. Unsupported drainage value: Reject values such as "unknown" or "GOOD".
6. Whitespace-only location ID: Reject it. Otherwise preserve the original valid ID in output.
7. Floating-point inputs: Compare directly against thresholds; no rounding before classification.
5. Test Cases
Every implementation must pass these tests with the same exact JSON values.
Test 1 — Low Risk
Input:
{"location_id":"BAKU-001","rainfall_mm":5,"water_level_cm":2,"drainage_status":"good"}
Expected Output:
{"location_id":"BAKU-001","risk_score":0,"risk_level":"Low"}
Test 2 — Medium Risk
Input:
{"location_id":"BAKU-002","rainfall_mm":20,"water_level_cm":12,"drainage_status":"good"}
Expected Output:
{"location_id":"BAKU-002","risk_score":35,"risk_level":"Medium"}
Test 3 — High Risk With Drainage Problems
Input:
{"location_id":"BAKU-003","rainfall_mm":35,"water_level_cm":28,"drainage_status":"partial"}
Expected Output:
{"location_id":"BAKU-003","risk_score":80,"risk_level":"High"}
Test 4 — Score Cap at 100
Input:
{"location_id":"BAKU-004","rainfall_mm":70,"water_level_cm":80,"drainage_status":"blocked"}
Expected Output:
{"location_id":"BAKU-004","risk_score":100,"risk_level":"High"}
Test 5 — Exact Threshold Boundary
Input:
{"location_id":"BAKU-005","rainfall_mm":30,"water_level_cm":0,"drainage_status":"good"}
Expected Output:
{"location_id":"BAKU-005","risk_score":30,"risk_level":"Medium"}
Test 6 — Negative Value
Input:
{"location_id":"BAKU-006","rainfall_mm":-1,"water_level_cm":10,"drainage_status":"good"}
Expected Output:
{"error":"Invalid input"}
Test 7 — Missing Field
Input:
{"location_id":"BAKU-007","rainfall_mm":10,"water_level_cm":15}
Expected Output:
{"error":"Invalid input"}
Test 8 — Invalid Data Type
Input:
{"location_id":"BAKU-008","rainfall_mm":"40","water_level_cm":25,"drainage_status":"blocked"}
Expected Output:
{"error":"Invalid input"}
6. Cross-Language Consistency Requirements
- Use exactly the same threshold tables and input validation in every language.
- Reject Boolean values as numbers, even in languages where Booleans are numeric subtypes.
- Do not silently convert strings into numbers or change the case of drainage values.
- Compare the parsed JSON outputs structurally; property ordering and insignificant whitespace do not matter.
- A test passes only when both the risk score and classification (or the error object) match the expected output.
