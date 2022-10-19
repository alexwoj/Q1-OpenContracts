import unittest
from opencontracts.contracts import Contract, Contracts


class TestOpenContracts(unittest.TestCase):

    def setUp(self):

        self.open_contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        self.renegotiated = [3]
        self.top_n = 3
        self.expected_open_contracts = [5, 4, 2]

    def test_get_top_N_open_contracts(self):

        contracts = Contracts()
        top_n_actual_open_contracts = contracts.get_top_N_open_contracts(self.open_contracts, self.renegotiated,
                                                                         self.top_n)

        self.assertEqual(self.expected_open_contracts, top_n_actual_open_contracts)
        self.assertIsInstance(top_n_actual_open_contracts, list)
