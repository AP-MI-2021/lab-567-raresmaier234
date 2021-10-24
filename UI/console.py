from Domain.obiect import toString
from Logic.CRUD import addObject, deleteObject, modifyObject


def printMenu ():
    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Afisare obiecte.")
    print("x. Iesire")


def uiAddObject(lista):
    id = input("Dati id: ")
    nume = input("Dati nume: ")
    descriere = input("Dati descriere: ")
    pret = float(input("Dati pret: "))
    locatie = input("Dati locatie: ")
    return addObject(id, nume, descriere, pret, locatie, lista)


def uiDeleteObject(lista):
    deleteId = input("Da-ti id-ul obiectului: ")
    return deleteObject(deleteId, lista)


def uiModifyObject(lista):
    id = input("Da-ti id-ul obiectului: ")
    nume = input("Da-ti nume: ")
    descriere = input("Da-ti descrierea: ")
    pret = float(input("Da-ti pretul: "))
    locatie = input("Da-ti locatia: ")
    return modifyObject(id, nume, descriere, pret, locatie, lista)


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runUI(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAddObject(lista)
        elif optiune == "2":
            lista = uiDeleteObject(lista)
        elif optiune == "3":
            lista = uiModifyObject(lista)
        elif optiune == "4":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")