import unittest

from core.missing.Context import Context
from missingrepo.Missing import Missing

from config.report.ConfigReporter import ConfigReporter
from tests.helper.repository.RepositoryHelper import MissingRepositoryHelper


class ConfigReporterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.missing_repository = MissingRepositoryHelper()
        self.reporter = ConfigReporter(self.missing_repository)
        self.test_missing = Missing('BTCOTC', Context.EXCHANGE, 'test', 'Missing config')

    def test_should_report_missing(self):
        self.reporter.report_missing(self.test_missing)
        self.reporter.delay_missing_storing()
        stored_missing = self.missing_repository.stored_values[0]
        self.assertEqual(self.test_missing, stored_missing)

    def test_should_not_report_missing_when_already_ignored(self):
        def ignored_check(missing: Missing):
            return missing.missing == 'BTCOTC'
        self.reporter.set_ignored_check_func(ignored_check)
        self.reporter.report_missing(self.test_missing)
        self.assertEqual(0, len(self.missing_repository.stored_values))
        self.assertNotIn(self.test_missing, self.missing_repository.stored_values)

    def test_should_report_missing_when_not_ignored(self):
        def ignored_check(missing: Missing):
            return missing.missing == 'SOMEOTHER'
        self.reporter.set_ignored_check_func(ignored_check)
        self.reporter.report_missing(self.test_missing)
        self.reporter.delay_missing_storing()
        self.assertEqual(1, len(self.missing_repository.stored_values))
        self.assertIn(self.test_missing, self.missing_repository.stored_values)

    def test_should_report_missing_and_call_function_post_reporting(self):
        self.callback_called = False
        def post_missing_report():
            self.callback_called = True
        self.reporter.report_missing(self.test_missing, post_missing_report)
        self.reporter.delay_missing_storing()
        stored_missing = self.missing_repository.stored_values[0]
        self.assertEqual(self.test_missing, stored_missing)
        self.assertTrue(self.callback_called)


if __name__ == '__main__':
    unittest.main()
