from Domain.obiect import getName, getId, getDescription, getPrice, getLocation
from Logic.CRUD import getById, addObject, deleteObject, modifyObject


def testAddObject():
    lista = []
    lista = addObject("1", "masca", "protectie", 200, "Lidl", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getName(getById("1", lista)) == "masca"
    assert getDescription(getById("1", lista)) == "protectie"
    assert getPrice(getById("1", lista)) == 200
    assert getLocation(getById("1", lista)) == "Lidl"


def testDeleteObject():
    lista = []
    lista = addObject("1", "ketchup", "iute", 12, "Cora", lista)
    lista = addObject("2", "pateu", "porc", 7, "Cora", lista)

    lista = deleteObject("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    assert len(lista) == 1
    assert getById("2", lista) is not None


def testModifyObject():
    lista = []
    lista = addObject("1", "cana", "cafea", 13, "Zara", lista)
    lista = addObject("2", "pahar", "plastic", 2, "Zara", lista)

    lista = modifyObject("1", "ibric", "metal", 10, "ccc", lista)

    updatedObj = getById("1", lista)
    assert getId(updatedObj) == "1"
    assert getName(updatedObj) == "ibric"
    assert getDescription(updatedObj) == "metal"
    assert getPrice(updatedObj) == 10
    assert getLocation(updatedObj) == "ccc"

    outdatedObj = getById("2", lista)
    assert getId(outdatedObj) == "2"
    assert getName(outdatedObj) == "pahar"
    assert getDescription(outdatedObj) == "plastic"
    assert getPrice(outdatedObj) == 2
    assert getLocation(outdatedObj) == "Zara"

    lista = []
    lista = addObject("2", "cana", "cafea", 13, "ccc", lista)

    lista = modifyObject("3", "ibric", "metal", 10, "ccc", lista)

    outdatedObj = getById("3", lista)
    assert getId(outdatedObj) == "3"
    assert getName(outdatedObj) == "cana"
    assert getDescription(outdatedObj) == "cafea"
    assert getPrice(outdatedObj) == 13
    assert getLocation(outdatedObj) == "ccc"
