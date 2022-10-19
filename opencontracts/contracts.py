class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:

    def __init__(self):
        pass

    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """Returns a list of top-n Associate Ids ordered by mount owed to the institution"""

        open_contracts_list = self._remove_renegotiated_contracts(open_contracts, renegotiated_contracts)
        ordered_open_contracts = self._order_open_contract_list(open_contracts_list)
        ordered_open_contracts_ranking = self._create_open_contracts_ranking(ordered_open_contracts, top_n)

        return ordered_open_contracts_ranking

    def _remove_renegotiated_contracts(self, open_contracts_obj, renegotiated_contracts):
        """Removes renegotiated contracts from open_contracts_obj and returns a list containing the
         Associate Id and Amount Owed to the institution"""

        open_contracts_list = []
        for contract in open_contracts_obj:
            if contract.id not in renegotiated_contracts:
                open_contracts_list.append([contract.id, contract.debt])

        return open_contracts_list

    def _order_open_contract_list(self, open_contracts):
        """Orders open contracts list by element [1] (owed value)"""

        return sorted(open_contracts, key=lambda x: x[1], reverse=True)

    def _create_open_contracts_ranking(self, ordered_open_contracts, top_n):

        ordered_open_contracts_ranking = []
        for contract in range(0, top_n):
            associate_id = ordered_open_contracts[contract][0]
            ordered_open_contracts_ranking.append(associate_id)

        return ordered_open_contracts_ranking
