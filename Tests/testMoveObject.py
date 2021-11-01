from Domain.obiect import getId, getName, getDescription, getPrice, getLocation
from Logic.CRUD import addObject, getByLocation
from Logic.moveObject import moveObject


def testMoveObject():
    lista = []
    lista = addObject("1", "cana", "cafea", 13, "Auchan", lista)
    lista = addObject("2", "pahar", "plastic", 2, "MegaImage", lista)

    nouaLocatie = "Carrefour"
    locatie = "Auchan"
    lista = moveObject(locatie, nouaLocatie, lista)
    locatie = getByLocation("Carrefour", lista)

    assert getLocation(locatie) == "Carrefour"
