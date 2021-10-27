from Domain.inventar import to_string
from Logic.CRUD import adauga_inventar, sterge_inventar, modificare_inventar


def print_menu():
    print("1.Adaugare inventar: ")
    print("2.Stergere inventar: ")
    print("3.Modificare inventar: ")
    print("a. Afiseaza toate inventarele: ")
    print("x. Iesire: ")


def ui_adaugare_inventar(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descriere: ")
    pret = float(input("Dati pret: "))
    locatie = input("Dati locatia: ")
    return adauga_inventar(id, nume, descriere, pret, locatie, lista)


def ui_stergere_inventar(lista):
    id = input("Dati id-ul inventarului de sters: ")
    return sterge_inventar(id, lista)



def ui_modificare_inventar(lista):
    id = input("Dati id-ul inventarului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret: "))
    locatie = input("Dati noua locatia: ")
    return modificare_inventar(id, nume, descriere, pret, locatie, lista)


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
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Ati ales o optiune gresit! Reincercati! ")
