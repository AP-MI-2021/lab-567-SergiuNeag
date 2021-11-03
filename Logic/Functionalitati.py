from Domain.inventar import get_locatie, creeaza_inventar, get_id, get_nume, get_descriere, get_pret


def muta_din_inventar(locatie, locatie_noua, lista):
    """
    Functia va cauta in lista, obiectele a caror locatie trebuie schimbata.
    Se va adauga in noua lista datele fiecarui obiect. In cazul in care se gaseste in lista
    un obiect a carui locatie trebuie schimbata, se va modifica locatia acestuia si se va adauga in noua lista.
    :param locatie: string
    :param locatie_noua: string
    :param lista: lista de obiecte
    :return:lista de obiecte dupa modificari
    """
    lista_noua = []
    for inventar in lista:
        if get_locatie(inventar) == locatie:
            inventar_nou = creeaza_inventar(get_id(inventar), get_nume(inventar), get_descriere(inventar), get_pret(inventar), locatie_noua)
            lista_noua.append(inventar_nou)
        else:
            lista_noua.append(inventar)
    return lista_noua


def concateneaza_string_pret_mai_mare(cuvant, val, lista):
    """
    Concateneaza un string(retinut in variabila cuvant) obiectelor (inventarelor)
    care au un pret mai mare decat floatul retinut in variabila val
    :param cuvant: Stringul care va fi concatenat obiectului
    :param val: Valoarea citita in functie de care concatenam
    :param lista: Lista de obiecte
    :return: Lista dupa modificarile aferente
    """
    lista_noua = []
    for inventar in lista:
        if get_pret(inventar) > val:
            inventar_nou = creeaza_inventar(get_id(inventar), get_nume(inventar), get_descriere(inventar) + cuvant,
                                            get_pret(inventar), get_locatie(inventar))
            lista_noua.append(inventar_nou)
        else:
            lista_noua.append(inventar)
    return lista_noua
