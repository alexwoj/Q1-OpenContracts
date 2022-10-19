from opencontracts.contracts import Contract, Contracts

contracts = Contracts()

contracts_object_list = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]



renegotiated_associate_ids = [3]
top_n = 3
actual_open_contracts = contracts.get_top_N_open_contracts(contracts_object_list, renegotiated_associate_ids,
                                                           top_n)
print(actual_open_contracts)