"""Executable acceptance examples using independent, fixed expected values."""

from datetime import date
import unittest

from loan import Loan, LoanRuleViolation, renew


class LoanRenewalTests(unittest.TestCase):
    def test_renewal_extends_existing_due_date(self):
        original = Loan(date(2030, 1, 10))

        result = renew(original, date(2030, 1, 2), 14)

        self.assertEqual(Loan(date(2030, 1, 24), renewal_count=1), result)

    def test_second_renewal_is_rejected(self):
        original = Loan(date(2030, 1, 24), renewal_count=1)

        with self.assertRaises(LoanRuleViolation):
            renew(original, date(2030, 1, 10), 14)

        self.assertEqual(Loan(date(2030, 1, 24), renewal_count=1), original)

    def test_returned_loan_is_rejected(self):
        original = Loan(date(2030, 1, 10), returned=True)

        with self.assertRaises(LoanRuleViolation):
            renew(original, date(2030, 1, 2), 14)

        self.assertEqual(Loan(date(2030, 1, 10), returned=True), original)

    def test_expired_loan_is_rejected(self):
        original = Loan(date(2030, 1, 10))

        with self.assertRaises(LoanRuleViolation):
            renew(original, date(2030, 1, 11), 14)

        self.assertEqual(Loan(date(2030, 1, 10)), original)

    def test_invalid_extension_is_rejected(self):
        for days in (0, -1, 1.5, True):
            with self.subTest(days=days):
                original = Loan(date(2030, 1, 10))

                with self.assertRaises(LoanRuleViolation):
                    renew(original, date(2030, 1, 2), days)

                self.assertEqual(Loan(date(2030, 1, 10)), original)

    def test_success_preserves_input_snapshot(self):
        original = Loan(date(2030, 1, 10))

        result = renew(original, date(2030, 1, 10), 14)

        self.assertIsNot(original, result)
        self.assertEqual(Loan(date(2030, 1, 10)), original)
        self.assertEqual(Loan(date(2030, 1, 24), renewal_count=1), result)


if __name__ == '__main__':
    unittest.main()
