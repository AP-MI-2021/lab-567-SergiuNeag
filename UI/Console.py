from Domain.inventar import to_string
from Logic.CRUD import adauga_inventar, sterge_inventar, modificare_inventar
from Logic.Functionalitati import muta_din_inventar, concateneaza_string_pret_mai_mare


def print_menu():
    print("1.Adaugare inventar: ")
    print("2.Stergere inventar: ")
    print("3.Modificare inventar: ")
    print("4.Muta in alta locatie: ")
    print("5.Concateneaza string dupa pret: ")
    print("a. Afiseaza toate inventarele: ")
    print("x. Iesire: ")


def ui_adaugare_inventar(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pret: "))
        locatie = input("Dati locatia: ")
        return adauga_inventar(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_inventar(lista):
    try:
        id = input("Dati id-ul inventarului de sters: ")
        return sterge_inventar(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_inventar(lista):
    try:
        id = input("Dati id-ul inventarului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatia: ")
        return modificare_inventar(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_muta_din_inventar(lista):
    try:
        locatie = input("Din ce locatie doresti sa muti?: ")
        locatie_noua = input("Locatia in care doresti sa muti: ")
        return muta_din_inventar(locatie, locatie_noua, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_concateneaza_string_pret_mai_mare(lista):
    cuvant = input("Stringul care va fi concatenat: ")
    val = float(input("Descrierea va fi concatenata pentru pretul mai mare de: "))
    return concateneaza_string_pret_mai_mare(cuvant, val, lista)


def show_all(lista):
    for inventar in lista:
        print(to_string(inventar))


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lista = ui_adaugare_inventar(lista)
        elif optiune == "2":
            lista = ui_stergere_inventar(lista)
        elif optiune == "3":
            lista = ui_modificare_inventar(lista)
        elif optiune == "4":
            lista = ui_muta_din_inventar(lista)
        elif optiune == "5":
            lista = ui_concateneaza_string_pret_mai_mare(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Ati ales o optiune gresit! Reincercati! ")
