from Domain.obiect import getDescription
from Logic.CRUD import addObject, getById
from Logic.concatenate import concatenateDescription


def test_concatenateDescription():
    lista = []
    lista = addObject("1", "masca", "protectie", 200, "Lidl", lista)
    pret = 300
    newDescription = "Covid"
    lista = concatenateDescription(lista, pret, newDescription)
    assert getDescription(getById("1", lista)) == "protectieCovid"

    lista = []
    lista = addObject("2", "roata", "masina", 200, "Lidl", lista)
    pret = 150
    newDescription = "Sport"
    rez = concatenateDescription(lista, pret, newDescription)
    assert getDescription(getById("2", rez)) == "masina"
    pret = 400
    rez = concatenateDescription(lista, pret, newDescription)
    assert getDescription(getById("2", rez)) == "masinaSport"
