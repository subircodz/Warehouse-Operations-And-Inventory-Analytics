# Design Decisions

This document captures the important engineering decisions made during the development of the Python Data Validation module.

The goal is simple: whenever I make a design choice that is not immediately obvious from the code, I record **what I chose, why I chose it, and what I expect from that decision**. This helps me understand my own reasoning when I revisit the project months later and also makes it easier for anyone exploring the repository to follow the project's evolution.

---

# Engineering Decision 01 — Single Entry Point for Data Loading

## Decision

Use a single public function:

```python
load_data(source)
```

instead of exposing multiple public functions such as:

- `read_excel()`
- `read_csv()`
- `read_json()`

## Why I Chose This

The application should not need to know how different file formats are loaded.

`load_data()` acts as a dispatcher. Its responsibility is to identify the file type and delegate the work to the appropriate reader.

This provides:

- A single public API
- Cleaner application code
- Easier future expansion when new file formats are added

## Alternative Considered

Expose individual reader functions directly.

## Why I Didn't Choose It

Doing so would make the application responsible for deciding which reader to call, increasing coupling between the application and file-loading logic.

---

# Engineering Decision 02 — Keep the Dispatcher Small

## Decision

`load_data()` is responsible only for:

- validating the source
- identifying the file type
- delegating to the correct reader

It is **not** responsible for reading worksheets or parsing data.

## Why I Chose This

Following the **Single Responsibility Principle (SRP)** keeps the dispatcher simple and easier to test.

---

# Engineering Decision 03 — Validate Before Delegating

## Decision

Each reader function (for example `read_excel()`) is responsible for:

- opening the file
- discovering worksheets
- loading worksheet data
- returning a dictionary of Pandas DataFrames

## Expected Return

```python
dict[str, pandas.DataFrame]
```

## Why I Chose This

The dispatcher should not know how individual file formats work. Each reader should fully own its parsing logic.

---

# Engineering Decision 04 — Validate Before Delegating

## Decision

Perform validation before calling any reader.

Validation order:

1. Verify source exists.
2. Verify supported file extension.
3. Delegate to the appropriate reader.

## Why I Chose This

Following the **Fail Fast** principle prevents unnecessary execution and immediately reports invalid input.

---

# Engineering Decision 05 — Raise Specific Exceptions

## Decision

Raise specific exceptions instead of returning `None`.

Examples:

- `FileNotFoundError`
- `PermissionError`
- `ValueError`

## Why I Chose This

Returning `None` allows the validation pipeline to continue in an invalid state.

Raising a specific exception immediately identifies the actual problem, simplifies debugging, and prevents downstream failures.

## Alternative Considered

Return `None` and allow the caller to handle the situation.

## Why I Didn't Choose It

Returning `None` hides the original problem and often results in unrelated errors later in the execution pipeline.

---

# Engineering Decision 06 — Test-Driven Development (TDD)

## Decision

Every new function will follow this workflow:

1. Write a failing unit test.
2. Run the test (RED).
3. Write the minimum production code.
4. Run the test (GREEN).
5. Refactor while keeping all tests passing.

## Why I Chose This

TDD encourages incremental development, reduces regressions, and provides executable documentation through unit tests.

---

# Engineering Decision 07 — One Behaviour Per Test

## Decision

Each unit test should verify only one behaviour.

## Why I Chose This

Smaller tests are easier to understand, maintain, and debug.

When a test fails, the broken behaviour can be identified immediately without investigating multiple conditions.

---

## Revision Notes

This document is intended to evolve alongside the project. New architectural or engineering decisions will be added as the project grows instead of modifying previous entries.