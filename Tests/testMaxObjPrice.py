from Domain.obiect import creeazaObiect
from Logic.CRUD import addObject
from Logic.maxObjectPrice import listLocation, maxObjectPrice


def test_listLocation():
    lista = []
    id = "1"
    nume = "pahar"
    descriere = "plastic"
    pret = 40
    locatie = "Lidl"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    id = "2"
    nume = "cana"
    descriere = "ceramica"
    pret = 50
    locatie = "Cora"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    id = "3"
    nume = "caiet"
    descriere = "mate"
    pret = 60
    locatie = "Cora"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    new_list = listLocation(lista)
    assert len(new_list) == 2
    assert new_list[0] == "Lidl"
    assert new_list[1] == "Cora"


def test_maxObjectPrice():
    lista = []
    id = "1"
    nume = "pahar"
    descriere = "plastic"
    pret = 40
    locatie = "Lidl"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    id = "2"
    nume = "cana"
    descriere = "ceramica"
    pret = 50
    locatie = "Cora"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    id = "3"
    nume = "caiet"
    descriere = "mate"
    pret = 60
    locatie = "Cora"
    lista = addObject(id, nume, descriere, pret, locatie, lista)

    lista = addObject("4", "laptop", "gaming", 8000, "eMAG", lista)

    assert maxObjectPrice("Cora") == 60
    assert maxObjectPrice("Lidl") == 40
    assert maxObjectPrice("eMAG") == 8000

