# Structured Bug Reports

This document contains structured reports for the five bugs identified, analyzed, and fixed during the AI debugging task.

## Bug 1: Syntax Error in Python

**File Name:** `bug1.py`  
**Fixed File:** `bug1_fixed.py`

### Bug Summary
The program was designed to check whether a person is an adult or a minor based on their age. However, it could not execute because of a syntax error.

### Root Cause
The `if` statement was missing a colon (`:`) at the end of the condition. Python requires a colon after conditional statements.

### Resolution
- **AI-Generated Suggestion:** Add the missing colon after `if age >= 18:`.
- **Manual Edits:** Applied the suggested correction to the fixed file. No additional manual changes were required.

### Lessons Learned
Python syntax rules must be followed precisely. Even a small syntax mistake, such as a missing colon, can prevent an entire program from running.

---

## Bug 2: Logical Error in JavaScript

**File Name:** `bug2.js`  
**Fixed File:** `bug2_fixed.js`

### Bug Summary
The program was intended to calculate the total price of products and apply a 10% discount. Instead, it increased the total price by 10%.

### Root Cause
The discount calculation used addition (`+`) instead of subtraction (`-`). As a result, the program applied an additional charge rather than reducing the price.

### Resolution
- **AI-Generated Suggestion:** Replace the addition operator with subtraction in the final price calculation.
- **Manual Edits:** Applied the suggested correction and retained the existing discount calculation structure.

### Lessons Learned
Logical errors may not cause syntax or runtime exceptions, but they can produce incorrect results. Understanding the intended business logic is essential when reviewing calculations.

---

## Bug 3: Runtime Exception in Python

**File Name:** `bug3.py`  
**Fixed File:** `bug3_fixed.py`

### Bug Summary
The program was designed to calculate the average of a list of numbers. However, it crashed when the input list was empty.

### Root Cause
The program attempted to divide the sum of the list by its length without checking whether the list contained any elements. An empty list has a length of zero, causing a `ZeroDivisionError`.

### Resolution
- **AI-Generated Suggestion:** Check whether the list is empty before performing the calculation. Raise a `ValueError` with a descriptive message and handle the exception using a `try-except` block.
- **Manual Edits:** Applied the suggested validation and exception-handling logic.

### Lessons Learned
Input validation is important for preventing runtime exceptions. Programs should handle edge cases, such as empty collections, before performing calculations.

---

## Bug 4: Off-by-One Error in C#

**File Name:** `bug4.cs`  
**Fixed File:** `bug4_fixed.cs`

### Bug Summary
The program was intended to print all elements of an integer array. However, it caused an `IndexOutOfRangeException` when accessing an invalid array index.

### Root Cause
The `for` loop used the condition `i <= numbers.Length` instead of `i < numbers.Length`. Since array indexes start at zero, the last valid index is `numbers.Length - 1`.

### Resolution
- **AI-Generated Suggestion:** Replace `i <= numbers.Length` with `i < numbers.Length`.
- **Manual Edits:** Applied the suggested loop-condition correction without changing the overall program structure.

### Lessons Learned
Array indexes must remain within valid boundaries. Using the correct loop condition helps prevent off-by-one errors and out-of-range exceptions.

---

## Bug 5: Data Type Misuse in JavaScript

**File Name:** `bug5.js`  
**Fixed File:** `bug5_fixed.js`

### Bug Summary
The program was intended to calculate the total quantity of products in multiple orders. Instead of returning the correct numerical total, it concatenated values as strings.

### Root Cause
The `quantity` properties were stored as strings rather than numbers. In JavaScript, the `+` operator performs string concatenation when one of its operands is a string.

### Resolution
- **AI-Generated Suggestion:** Store quantity values as numbers instead of strings.
- **Manual Edits:** Updated the quantity values in the order objects to numeric values.

### Lessons Learned
Choosing the correct data type is essential for accurate calculations. Developers should validate input types and understand how operators behave with different data types.

---

## Overall Conclusion

This debugging exercise demonstrated how AI tools can help identify syntax errors, logical errors, runtime exceptions, off-by-one errors, and data type misuse.

The AI-generated suggestions provided solutions for all five bugs. Applying and reviewing these fixes also highlighted the importance of understanding the root cause, validating input data, handling edge cases, and testing the corrected code.

AI can accelerate debugging, but developers should always review suggested changes and verify that the fixes produce the expected results.
