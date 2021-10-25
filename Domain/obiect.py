def creeazaObiect(id, nume, descriere, pret, locatie):
    """
    creeaza o lista ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: dictionarul obiectului
    """
    return [id, nume, descriere, pret, locatie]


def getId (obiect):
    return obiect[0]


def getName (obiect):
    return obiect[1]


def getDescription (obiect):
    return obiect[2]


def getPrice (obiect):
    return obiect[3]


def getLocation(obiect):
    return obiect[4]


def toString (obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getName(obiect),
        getDescription(obiect),
        getPrice(obiect),
        getLocation(obiect)
    )
