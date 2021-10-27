from Tests.test_crud import test_adauga_inventar, test_sterge_inventar
from Tests.test_domain import test_inventar


def run_all_tests():
    test_inventar()
    test_adauga_inventar()
    test_sterge_inventar()