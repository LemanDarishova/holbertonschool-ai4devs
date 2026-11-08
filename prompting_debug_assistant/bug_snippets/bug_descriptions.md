# Bug Descriptions

## Bug 1 – bug1.py

**Intended Behavior:**  
Check whether a user is an adult or a minor based on their age.

**Issue Type:**  
Syntax Error.

**Notes:**  
The `if` statement is missing a colon, causing a SyntaxError when the program runs.

---

## Bug 2 – bug2.js

**Intended Behavior:**  
Calculate the total price of products and apply a 10% discount.

**Issue Type:**  
Logical Error.

**Notes:**  
The program adds 10% to the total price instead of subtracting the discount.

---

## Bug 3 – bug3.py

**Intended Behavior:**  
Calculate the average of numbers in a list.

**Issue Type:**  
Runtime Exception.

**Notes:**  
The function attempts to divide by zero when the input list is empty, resulting in a ZeroDivisionError.

---

## Bug 4 – bug4.cs

**Intended Behavior:**  
Print all elements of an integer array.

**Issue Type:**  
Off-by-one Error.

**Notes:**  
The loop condition allows the index to exceed the last valid array index, causing an IndexOutOfRangeException.

---

## Bug 5 – bug5.js

**Intended Behavior:**  
Calculate the total quantity of products in a list of orders.

**Issue Type:**  
Data Type Misuse.

**Notes:**  
The quantity values are stored as strings instead of numbers. As a result, the `+` operator concatenates strings rather than performing numerical addition.
