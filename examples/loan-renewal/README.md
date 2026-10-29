# Worked example: one loan renewal

This is a synthetic, self-contained example of a domain rule flowing into a specification, implementation, and executable acceptance. It is not a production lending system or an installed OpenSpec/Superpowers adapter.

## Domain language and ownership

- **Loan:** a snapshot of a borrowed item's current due date, renewal count, and returned state.
- **Renewal:** extending the existing due date once; it does not mean opening a new loan or starting the extension from today's date.
- **Rule owner:** the renewal operation owns eligibility and returns a new snapshot. A rejection leaves the caller's snapshot unchanged.

For brevity, dates are Python `date` values and snapshots supplied by this example contain the stated fields. Persistence, concurrent requests, authentication, snapshot construction validation, and calendar/time-zone policy are outside this increment.

## Behavioral specification

**Requirement: renew an eligible loan once.**

1. An unreturned loan with no prior renewal can be renewed on or before its due date.
2. The new due date is the existing due date plus the requested positive, whole number of days; its renewal count becomes one.
3. A second renewal, a returned loan, an expired loan, or an invalid extension is rejected.
4. The input snapshot is unchanged on both success and rejection.

| Scenario | Given / when / then | Executable test |
| --- | --- | --- |
| Extend the existing term | Given due January 10, renew on January 2 for 14 days; due January 24, count one | `test_renewal_extends_existing_due_date` |
| Reject a second renewal | Given count one, another renewal is rejected without changing the snapshot | `test_second_renewal_is_rejected` |
| Reject a returned loan | Given a returned loan, renewal is rejected without changing the snapshot | `test_returned_loan_is_rejected` |
| Reject an expired loan | Given due January 10, renew January 11; rejection preserves the snapshot | `test_expired_loan_is_rejected` |
| Reject an invalid extension | Given zero, negative, fractional, or boolean days, reject and preserve the snapshot | `test_invalid_extension_is_rejected` |
| Preserve input on success | Given an eligible snapshot, successful renewal returns a different snapshot and leaves the original unchanged | `test_success_preserves_input_snapshot` |

Dates in the example are fixed synthetic values, not current-time claims.

## Handoff to implementation

```text
Change: allow one eligible renewal
Inputs: Loan snapshot, today's date, positive whole-day extension
Output: renewed snapshot, or LoanRuleViolation
Domain constraints: one renewal, unreturned, not expired, input unchanged
Scope: only the pure renewal operation and the listed scenarios
Verification: six unittest cases in test_loan.py
```

OpenSpec can own this requirement and its change lifecycle; domain modeling owns the definitions and rule meaning; the implementation workflow consumes that contract. These responsibilities can be represented in the project's existing artifacts rather than copying this example's document layout.

## Run

From this directory:

```sh
python -m unittest discover -s . -p 'test_*.py' -v
```

From the repository root, `python scripts/validate.py` runs the same example plus package checks.

## A useful conflict to investigate

Suppose an implementation extends from today instead of from the existing due date, while an old test agrees with it. Compare the effective behavioral requirement and independently derived dates. The fact that implementation and test agree does not override the contract. Correct the wrong oracle or implementation with evidence, then recheck all retained scenarios.

If the product instead intentionally switches to “extend from today,” first specify that observable change and its compatibility consequences; do not silently change a test just to obtain GREEN.
