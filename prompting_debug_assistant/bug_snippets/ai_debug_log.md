# AI Debug Log

## Bug 1 – bug1.py

**AI Diagnosis:**

The `if` statement is missing a colon (`:`) at the end of the condition. Python requires a colon after conditional statements such as `if`, `else`, and `elif`. This causes a SyntaxError and prevents the program from running.

**Suggested Fix:**

Add a colon after `if age >= 18`.

```python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


def main():
    age = 22
    result = check_age(age)
    print("User status:", result)


main()
```

**Alternative Fixes Tested:** None.

**Result:**

The syntax error is resolved. The program runs successfully and prints `User status: Adult` when the age is 22.

---

## Bug 2 – bug2.js

**AI Diagnosis:**

The program uses the addition operator (`+`) when calculating the discount. Instead of subtracting 10% from the total price, it increases the price by 10%. This is a logical error because the calculation does not match the intended behavior.

**Suggested Fix:**

Replace the addition operator (`+`) with the subtraction operator (`-`) in the final price calculation.

```javascript
function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }

    let discount = 10;
    let finalPrice = total - (total * discount / 100);

    return finalPrice;
}

const products = [100, 200, 300];

console.log("Final price:", calculateTotal(products));
```

**Alternative Fixes Tested:** None.

**Result:**

The logical error is fixed. The total price is 600, and after applying a 10% discount, the correct final price is 540.

---

## Bug 3 – bug3.py

**AI Diagnosis:**

The function attempts to divide the sum of the numbers by the length of the list. However, when the list is empty, its length is zero. Dividing by zero raises a ZeroDivisionError.

**Suggested Fix:**

Check whether the list is empty before performing the division. Raise a ValueError with a descriptive message if no numbers are provided. Handle the exception in the main function.

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    total = sum(numbers)
    count = len(numbers)

    average = total / count

    return average


def main():
    numbers = []

    try:
        result = calculate_average(numbers)
        print("Average:", result)
    except ValueError as error:
        print("Error:", error)


main()
```

**Alternative Fixes Tested:** None.

**Result:**

The program no longer crashes with a ZeroDivisionError. When the list is empty, it displays a descriptive error message instead of attempting division.

---

## Bug 4 – bug4.cs

**AI Diagnosis:**

The `for` loop uses the condition `i <= numbers.Length`. Array indexes start at zero, so the last valid index is `numbers.Length - 1`. Using `<=` allows the loop to access an index outside the array boundaries, causing an IndexOutOfRangeException.

**Suggested Fix:**

Change the loop condition from `i <= numbers.Length` to `i < numbers.Length`.

```csharp
using System;

class Program
{
    static void PrintNumbers(int[] numbers)
    {
        for (int i = 0; i < numbers.Length; i++)
        {
            Console.WriteLine(numbers[i]);
        }
    }

    static void Main()
    {
        int[] values = { 10, 20, 30, 40, 50 };

        PrintNumbers(values);
    }
}
```

**Alternative Fixes Tested:** None.

**Result:**

The off-by-one error is fixed. The program successfully prints all five array elements without throwing an IndexOutOfRangeException.

---

## Bug 5 – bug5.js

**AI Diagnosis:**

The `quantity` properties are stored as strings instead of numbers. In JavaScript, the `+` operator performs string concatenation when one of the operands is a string. As a result, the program concatenates the quantities instead of calculating their numerical sum.

**Suggested Fix:**

Store the quantity values as numbers by removing the quotation marks around them.

```javascript
function calculateQuantity(orders) {
    let totalQuantity = 0;

    for (let i = 0; i < orders.length; i++) {
        totalQuantity += orders[i].quantity;
    }

    return totalQuantity;
}

const orders = [
    { product: "Laptop", quantity: 2 },
    { product: "Mouse", quantity: 3 },
    { product: "Keyboard", quantity: 1 }
];

console.log("Total quantity:", calculateQuantity(orders));
```

**Alternative Fixes Tested:** None.

**Result:**

The data type issue is resolved. JavaScript now performs numerical addition instead of string concatenation. The correct total quantity is 6.
