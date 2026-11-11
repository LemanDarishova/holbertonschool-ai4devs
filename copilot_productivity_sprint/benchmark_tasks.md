AI Coding Assistant Benchmark Tasks
Overview
These three beginner-friendly Python tasks are designed to compare AI coding assistants under similar conditions. Each task should take approximately 15–30 minutes. Implement each task independently and check the acceptance criteria before marking it complete.

Language: Python 3
Environment: Cursor or another Python-capable code editor
External packages: None required (Python standard library only)
Task 1 — Calculator Function
Estimated Time: 15–20 minutes
Suggested File: calculator.py

Requirements:
- Implement a function calculate(a, b, operation).
- Support four operations: add, subtract, multiply, and divide.
- Handle unsupported operations and division by zero without crashing.
Inputs:
- a and b: integers or floats.
- operation: one of "add", "subtract", "multiply", "divide".
- Example: calculate(10, 2, "divide").
Outputs:
- Return the numeric result for a valid operation.
- Return "Error: Division by zero" when dividing by zero.
- Return "Error: Invalid operation" for an unsupported operation.
- Example output: 5.0.
Acceptance Criteria:
1. calculate(8, 3, "add") returns 11.
2. calculate(10, 2, "divide") returns 5.0.
3. calculate(5, 0, "divide") returns "Error: Division by zero".
4. calculate(2, 3, "power") returns "Error: Invalid operation".
Task 2 — To-Do List Manager
Estimated Time: 20–30 minutes
Suggested File: todo.py

Requirements:
- Implement a class TodoList that initially contains no tasks.
- Provide add_task(title), complete_task(task_id), and list_tasks() methods.
- Assign each new task a unique positive integer ID starting at 1.
- Reject an empty or whitespace-only title and return False when trying to complete a nonexistent task.
Inputs:
- add_task(title): a string task title.
- complete_task(task_id): an integer ID.
- list_tasks(): no arguments.
- Example: todo.add_task("Study Python").
Outputs:
- add_task returns the created task dictionary, or None for an invalid title.
- complete_task returns True when successful and False if the ID does not exist.
- list_tasks returns a list of dictionaries in insertion order, each with id, title, and completed fields.
- Example task: {"id": 1, "title": "Study Python", "completed": False}.
Acceptance Criteria:
1. Adding "Study Python" creates task ID 1 with completed: False.
2. Completing task ID 1 returns True and changes its completed value to True.
3. Completing task ID 999 returns False without changing existing tasks.
4. Adding "   " returns None, and the task list remains unchanged.
Task 3 — Flood Risk Classifier
Estimated Time: 15–25 minutes
Suggested File: flood_risk.py

Requirements:
- Implement a function classify_flood_risk(water_level_cm, rainfall_mm).
- Use simple predefined thresholds to classify a monitoring location as "Low", "Medium", or "High".
- Return "Invalid input" for negative measurements or nonnumeric values.
- The function is a benchmark exercise, not a real flood prediction model.
Inputs:
- water_level_cm: measured water depth in centimeters.
- rainfall_mm: measured rainfall in millimeters.
- Example: classify_flood_risk(45, 30).
Outputs and Rules:
- "High" if water_level_cm >= 50 or rainfall_mm >= 40.
- Otherwise, "Medium" if water_level_cm >= 20 or rainfall_mm >= 15.
- Otherwise, "Low".
- "Invalid input" if either value is negative or nonnumeric (including Boolean values).
- Example output: "Medium".
Acceptance Criteria:
1. classify_flood_risk(10, 5) returns "Low".
2. classify_flood_risk(25, 10) returns "Medium".
3. classify_flood_risk(50, 5) returns "High", and classify_flood_risk(5, 40) also returns "High".
4. classify_flood_risk(-1, 10) and classify_flood_risk("unknown", 10) return "Invalid input".
Benchmark Procedure
For a fair comparison, use the same task descriptions and acceptance criteria with each AI assistant.
1. Start a separate coding session for each task.
2. Give the assistant the task's requirements, inputs, outputs, and acceptance criteria.
3. Record the time taken, number of prompts, and whether all acceptance criteria pass.
4. Review the generated code and note any manual corrections.
Task	Estimated Time	Actual Time	Acceptance Criteria Passed	AI Prompts Used
Calculator Function	15–20 min	To be measured	To be tested	To be counted
To-Do List Manager	20–30 min	To be measured	To be tested	To be counted
Flood Risk Classifier	15–25 min	To be measured	To be tested	To be counted


The results table is intentionally unfilled until you run the benchmarks; the tasks themselves are fully specified above.
