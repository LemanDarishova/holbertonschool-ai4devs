# Bug Snippet Descriptions

This document describes the intended behavior and identified issue types of the intentionally flawed C# code snippets created for a payment processing microservice.

## Bug 1 – bug1.cs

**Intended Behavior:** Process payments within a predefined timeout limit and prevent operations from exceeding the allowed processing time.

**Issue Type:** Logical Error – Incorrect Timeout Handling.

**Notes:** The timeout is checked only after all payment operations are completed. Slow operations can exceed the configured timeout without being interrupted.

## Bug 2 – bug2.cs

**Intended Behavior:** Send user emails, merchant webhooks, and analytics updates efficiently without unnecessarily delaying payment processing.

**Issue Type:** Performance Issue – Sequential Asynchronous Processing.

**Notes:** Independent notification operations are executed sequentially, increasing the total processing time.

## Bug 3 – bug3.cs

**Intended Behavior:** Evaluate all fraud detection rules and reject a payment if any rule identifies suspicious activity.

**Issue Type:** Logical Error – Incorrect Loop Control.

**Notes:** The method returns false immediately after the first non-blocking rule, preventing the remaining fraud rules from being evaluated.

## Bug 4 – bug4.cs

**Intended Behavior:** Retry failed payment requests safely without charging customers multiple times for the same transaction.

**Issue Type:** Logical Error – Missing Idempotency Handling.

**Notes:** The payment gateway may successfully process a transaction even if the client receives a timeout. Retrying without an idempotency key can result in duplicate charges.

## Bug 5 – bug5.cs

**Intended Behavior:** Process gateway responses safely and handle missing or invalid responses without causing unexpected application crashes.

**Issue Type:** Runtime Exception – NullReferenceException.

**Notes:** The gateway response is not checked for null before accessing its properties, causing a runtime exception.

## Conclusion

These snippets represent common problems in payment processing systems, including timeout management, asynchronous execution, fraud detection, retry mechanisms, and null handling.

They will be used to investigate how AI-assisted debugging can identify root causes, suggest solutions, and improve backend application reliability.
