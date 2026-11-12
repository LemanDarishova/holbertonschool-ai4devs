# Pull Request: Add Code Review Severity Summary

## Summary

This PR introduces a Code Review Severity Summary feature that analyzes code review findings and groups them by severity level: Critical, High, Medium, and Low.

It provides a structured summary showing the total number of issues and helps developers identify the most important problems that need attention.

## Changes

- Added a new severity summary module.
- Implemented issue classification by severity.
- Added issue counting for each severity level.
- Added validation for invalid or missing severity values.
- Added an overall issue count.
- Added unit tests for severity classification and summary generation.

## Context

During code reviews, developers may receive multiple findings with different levels of importance. Without a structured summary, it can be difficult to prioritize issues.

This feature makes the review process more organized and helps developers focus on critical problems first.

**Estimated implementation:** 100–200 LOC.

**Related issue:** Code review reporting and issue prioritization improvement.
