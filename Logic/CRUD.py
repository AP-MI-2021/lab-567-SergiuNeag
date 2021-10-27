from Domain.inventar2 import creeaza_inventar, get_id


def adauga_inventar(id, nume, descriere, pret, locatie, lista):
    """
    Adauga un inventar intr-o lista
    :param id: string
    :param nume:string
    :param descriere:string
    :param pret:float
    :param locatie:string
    :param lista:lista de inventare
    :return: o lista continand elementele vechi si noul inventar
    """
    inventar = creeaza_inventar(id, nume, descriere, pret, locatie)
    return lista + [inventar]


def get_by_id(id, lista):
    """
    un inventar cu id-ul dat
    :param id: string
    :param lista: lista de inventare
    :return: inventarul cu id-ul dat sau None daca nu exista
    """
    for inventar in lista:
        if get_id(inventar) == id:
            return inventar
    return None

def sterge_inventar(id, lista):
    """
    sterge un inventar dintr-o lista
    :param id:
    :param lista:
    :return:
    """
    return [inventar for inventar in lista if get_id(inventar) != id]


def modificare_inventar(id, nume, descriere, pret, locatie, lista):
    """

    :param id: Id-ul dupa care se modifica
    :param nume: noul nume
    :param descriere: noua descriere
    :param pret: noul pret
    :param locatie: noua locatie
    :param lista: noua lista
    :return:
    """
    lista_noua = []
    for inventar in lista:
        if get_id(inventar) == id:
            inventar_nou = creeaza_inventar(id, nume, descriere, pret, locatie)
            lista_noua.append(inventar_nou)
        else:
            lista_noua.append(inventar)
    return lista_noua