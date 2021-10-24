from Domain.obiect import creeazaObiect, getId, getName, getDescription, getPrice, getLocation


def testObiect():
    obiect = creeazaObiect("1", "cana", "plastic", 20, "Profi")
    assert getId(obiect) == "1"
    assert getName(obiect) == "cana"
    assert getDescription(obiect) == "plastic"
    assert getPrice(obiect) == 20
    assert getLocation(obiect) == "Profi"