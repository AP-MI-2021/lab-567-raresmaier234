def creeazaObiect(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: dictionarul obiectului
    """
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }


def getId (obiect):
    return obiect["id"]


def getName (obiect):
    return obiect["nume"]


def getDescription (obiect):
    return obiect["descriere"]


def getPrice (obiect):
    return obiect["pret"]


def getLocation(obiect):
    return obiect["locatie"]


def toString (obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getName(obiect),
        getDescription(obiect),
        getPrice(obiect),
        getLocation(obiect)
    )
