from Domain.inventar import get_locatie, get_descriere
from Logic.CRUD import adauga_inventar
from Logic.Functionalitati import muta_din_inventar, concateneaza_string_pret_mai_mare, cel_mai_mare_pret_locatie


def test_muta_din_inventar():
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "literatura", 25, "e2", lista)
    lista = muta_din_inventar("e2", "e5", lista)
    lista = muta_din_inventar("e1", "e6", lista)
    assert get_locatie(lista[0]) == "e6"
    assert get_locatie(lista[1]) == "e5"
    assert get_locatie(lista[1]) != "e6"


def test_concateneaza_string_pret_mai_mare():
    lista = []
    lista = adauga_inventar("1", "carte", "li", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "li", 25, "e2", lista)
    lista = adauga_inventar("3", "carte", "li", 5, "e3", lista)
    lista = concateneaza_string_pret_mai_mare("SSS", 5, lista)
    assert get_descriere(lista[0]) == "liSSS"
    assert get_descriere(lista[1]) == "liSSS"
    assert get_descriere(lista[2]) == "li"


def test_cel_mai_mare_pret_locatie():
    lista = []
    lista = adauga_inventar("1", "carte", "li", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "li", 25, "e2", lista)
    lista = adauga_inventar("3", "carte", "li", 5, "e1", lista)
    assert cel_mai_mare_pret_locatie(lista) == {"e1": 10, "e2": 25}
    lista = adauga_inventar("4", "carte", "li", 40, "e2", lista)
    assert cel_mai_mare_pret_locatie(lista) == {"e1": 10, "e2": 40}
