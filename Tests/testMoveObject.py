from Domain.obiect import getId, getName, getDescription, getPrice, getLocation
from Logic.CRUD import addObject, getByLocation
from Logic.moveObject import moveObject


def testMoveObject():
    lista = []
    lista = addObject("1", "cana", "cafea", 13, "dm", lista)
    lista = addObject("2", "pahar", "plastic", 2, "c&a", lista)

    nouaLocatie = "c&a"
    locatie = "dm"
    lista = moveObject(locatie, nouaLocatie, lista)
    locatie = getByLocation("c&a", lista)

    assert getLocation(locatie) == "c&a"
