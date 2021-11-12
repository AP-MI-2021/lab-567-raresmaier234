from Domain.obiect import toString, getLocation
from Logic.CRUD import addObject, deleteObject, modifyObject
from Logic.concatenate import concatenateDescription
from Logic.maxObjectPrice import maxObjectPrice, listLocation
from Logic.moveObject import moveObject
from Logic.priceSort import sortPrices
from Logic.sumPrices import sumPrices
from UI.command import menu


def printMenu ():
    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Modificare locatie a obiectelor.")
    print("5. Determinarea pretului maxim al unui obiect din depozit.")
    print("6. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("7. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("8. Concatenarea unui string citit la toate descrierile obiectelor cu prețul"
          "  mai mare decât o valoare citită.")
    print("a. Afisare obiecte.")
    print("u. Undo.")
    print("r. Redo.")
    print("x. Iesire.")


def uiAddObject(lista, undoList, redoList):
    try:
        id = input("Dati id: ")
        nume = input("Dati nume: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pret: "))
        locatie = input("Dati locatie: ")
        rez = addObject(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rez
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDeleteObject(lista, undoList, redoList):
    try:
        deleteId = input("Da-ti id-ul obiectului: ")
        rez = deleteObject(deleteId, lista)
        undoList.append(lista)
        redoList.clear()
        return rez
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModifyObject(lista, undoList, redoList):
    try:
        id = input("Da-ti id-ul obiectului: ")
        nume = input("Da-ti nume: ")
        descriere = input("Da-ti descrierea: ")
        pret = float(input("Da-ti pretul: "))
        locatie = input("Da-ti locatia: ")
        rez = modifyObject(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rez
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiNewLocationObject(lista, undoList, redoList):
    try:
        locatie = input("Da-ti locatia curenta a obiectelor: ")
        nouaLocatie = input("Da-ti locatia unde doriti sa fie mutate obiectele: ")
        rez = moveObject(locatie, nouaLocatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rez
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


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


def uiConcatenateDescription(lista, undoList, redoList):
    try:
        description = input("Scrieti descrierea: ")
        pret = float(input("Dati valoarea: "))
        undoList.append(lista)
        redoList.append(concatenateDescription(lista, pret, description))
        showAll(concatenateDescription(lista, pret, description))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runUI(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAddObject(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiDeleteObject(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModifyObject(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiNewLocationObject(lista, undoList, redoList)
        elif optiune == "5":
            uiMaxPriceObj(lista)
        elif optiune == "6":
            uiSortPrices(lista)
        elif optiune == "7":
            uiSumPrices(lista)
        elif optiune == "8":
            uiConcatenateDescription(lista, undoList, redoList)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Eroare: nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Eroare: nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
