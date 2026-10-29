"""Pure domain behavior for the synthetic loan-renewal example."""

from dataclasses import dataclass, replace
from datetime import date, timedelta


class LoanRuleViolation(ValueError):
    """A requested renewal violates the stated behavioral contract."""


@dataclass(frozen=True)
class Loan:
    due_date: date
    renewal_count: int = 0
    returned: bool = False


def renew(loan: Loan, today: date, extension_days: int) -> Loan:
    """Renew according to the example contract."""
    if isinstance(extension_days, bool) or not isinstance(extension_days, int) or extension_days <= 0:
        raise LoanRuleViolation('The extension must be a positive whole number of days.')
    if loan.returned:
        raise LoanRuleViolation('A returned loan cannot be renewed.')
    if loan.renewal_count >= 1:
        raise LoanRuleViolation('Only one renewal is allowed.')
    if today > loan.due_date:
        raise LoanRuleViolation('An expired loan cannot be renewed.')

    return replace(loan, due_date=loan.due_date + timedelta(days=extension_days), renewal_count=1)
