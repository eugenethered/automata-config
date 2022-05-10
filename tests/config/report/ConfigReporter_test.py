import unittest

from core.market.Market import Market
from core.missing.Context import Context
from missingrepo.Missing import Missing

from config.report.ConfigReporter import ConfigReporter
from tests.helper.repository.RepositoryHelper import MissingRepositoryHelper


class ConfigReporterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.missing_repository = MissingRepositoryHelper()
        self.reporter = ConfigReporter(self.missing_repository)

    def test_should_report_missing(self):
        missing = Missing('BTCOTC', Context.EXCHANGE, Market.BINANCE, 'Missing config')
        self.reporter.report_missing(missing)
        stored_missing = self.missing_repository.stored_values[0]
        self.assertEqual(missing, stored_missing)


if __name__ == '__main__':
    unittest.main()
