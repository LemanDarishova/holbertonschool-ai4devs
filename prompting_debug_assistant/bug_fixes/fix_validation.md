# Fix Validation Report

## Bug 1 – bug1_fixed.py

**Test Case 1:**

- **Input:** `age = 22`
- **Expected Output:** `Adult`
- **Actual Output:** `Adult` ✅

**Test Case 2:**

- **Input:** `age = 16`
- **Expected Output:** `Minor`
- **Actual Output:** `Minor` ✅

**Test Result:** All test cases passed.

---

## Bug 2 – bug2_fixed.js

**Test Case 1:**

- **Input:** `[100, 200, 300]`
- **Expected Output:** `540`
- **Actual Output:** `540` ✅

**Test Case 2:**

- **Input:** `[100]`
- **Expected Output:** `90`
- **Actual Output:** `90` ✅

**Test Result:** All test cases passed.

---

## Bug 3 – bug3_fixed.py

**Test Case 1:**

- **Input:** `[10, 20, 30]`
- **Expected Output:** `20.0`
- **Actual Output:** `20.0` ✅

**Test Case 2:**

- **Input:** `[]`
- **Expected Output:** `ValueError: The list cannot be empty.`
- **Actual Output:** `ValueError: The list cannot be empty.` ✅

**Test Result:** All test cases passed.

---

## Bug 4 – bug4_fixed.cs

**Test Case 1:**

- **Input:** `[10, 20, 30, 40, 50]`
- **Expected Output:**
  ```text
  10
  20
  30
  40
  50
  ```
- **Actual Output:**
  ```text
  10
  20
  30
  40
  50
  ```
  ✅

**Test Case 2:**

- **Input:** `[100]`
- **Expected Output:**
  ```text
  100
  ```
- **Actual Output:**
  ```text
  100
  ```
  ✅

**Test Result:** All test cases passed.

---

## Bug 5 – bug5_fixed.js

**Test Case 1:**

- **Input:** 
  ```javascript
  [
      { product: "Laptop", quantity: 2 },
      { product: "Mouse", quantity: 3 },
      { product: "Keyboard", quantity: 1 }
  ]
  ```
- **Expected Output:** `6`
- **Actual Output:** `6` ✅

**Test Case 2:**

- **Input:**
  ```javascript
  [
      { product: "Monitor", quantity: 5 },
      { product: "Mouse", quantity: 2 }
  ]
  ```
- **Expected Output:** `7`
- **Actual Output:** `7` ✅

**Test Result:** All test cases passed.

---

## Final Summary

| Bug | Error Type | Validation |
|---|---|---|
| Bug 1 | Syntax Error | Passed |
| Bug 2 | Logical Error | Passed |
| Bug 3 | Runtime Exception | Passed |
| Bug 4 | Off-by-one Error | Passed |
| Bug 5 | Data Type Misuse | Passed |

**Overall Result:** All five fixes have corresponding test cases and expected outputs. No additional manual changes beyond the documented fixes were required.
