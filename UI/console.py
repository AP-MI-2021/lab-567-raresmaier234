from Domain.obiect import toString, getLocation
from Logic.CRUD import addObject, deleteObject, modifyObject
from Logic.concatenate import concatenateDescription
from Logic.maxObjectPrice import maxObjectPrice, listLocation
from Logic.moveObject import moveObject
from Logic.priceSort import sortPrices
from Logic.sumPrices import sumPrices


def printMenu ():
    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Afisare obiecte.")
    print("5. Modificare locatie a obiectelor.")
    print("6. Determinarea pretului maxim al unui obiect din depozit.")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("9. Concatenarea unui string citit la toate descrierile obiectelor cu prețul"
          "  mai mare decât o valoare citită.")
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


def uiNewLocationObject(lista):
    locatie = input("Da-ti locatia curenta a obiectelor: ")
    nouaLocatie = input("Da-ti locatia unde doriti sa fie mutate obiectele: ")
    return moveObject(locatie, nouaLocatie, lista)


def uiMaxPriceObj(lista):
    listLocations = listLocation(lista)
    listPrices = maxObjectPrice(lista)
    for obiect in range(0, len(listLocations)):
        print(listLocations[obiect], ":", listPrices[obiect])


def uiSortPrices(lista):
    rezultat = sortPrices(lista)
    showAll(rezultat)


def uiSumPrices(lista):
    rezultat = sumPrices(lista)
    for location in rezultat:
        print(location, ":", rezultat[location])


def uiConcatenateDescription(lista):
    description = input("Scrieti descrierea: ")
    pret = float(input("Dati valoarea: "))
    showAll(concatenateDescription(lista, pret, description))


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
        elif optiune == "5":
            lista = uiNewLocationObject(lista)
        elif optiune == "6":
            uiMaxPriceObj(lista)
        elif optiune == "7":
            uiSortPrices(lista)
        elif optiune == "8":
            uiSumPrices(lista)
        elif optiune == "9":
            uiConcatenateDescription(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
