# Bug Descriptions

These snippets are intentionally flawed. Each file demonstrates a different type of bug.
The expected behavior is documented below; the code should be analyzed before making fixes.

## bug1.py
- Language: Python
- Intended Behavior: Return the last n items from a list. If n is zero or negative, return an empty list.
- Current Issue: The slice start index is calculated one position too early. The n == 0 case also incorrectly returns the last item.

## bug2.js
- Language: JavaScript
- Intended Behavior: Calculate and return the arithmetic average of all numbers. Return 0 for an empty array.
- Current Issue: The loop condition uses <= instead of <, so it reads one position beyond the end of the array. This adds undefined to the total and causes the result to become NaN.

## bug3.java
- Language: Java
- Intended Behavior: Count every even number in the given integer array.
- Current Issue: The loop stops before the final array element, so an even value in the last position is ignored.

## bug4.cs
- Language: C#
- Intended Behavior: Return true if the password is at least 8 characters long and contains at least one digit; otherwise return false.
- Current Issue: The length comparison is too strict (> 8 rather than >= 8) and the digit condition is reversed.

## bug5.py
- Language: Python
- Intended Behavior: Find a user by ID and return the matching user dictionary. Return None when no user is found.
- Current Issue: The function returns an empty dictionary instead of None when the requested ID does not exist.
