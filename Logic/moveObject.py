from Domain.obiect import getLocation, getPrice, getDescription, getName, getId, creeazaObiect
from Logic.CRUD import modifyObject, getByLocation


def moveObject(locatie, unde_locatie, lista):
    """
    Functia va cauta in lista, obiectele a caror locatie trebuie schimbata.
    Se va adauga in noua lista datele fiecarui obiect. In cazul in care se gaseste in lista
    un obiect a carui locatie trebuie schimbata, se va modifica locatia acestuia si se va adauga in noua lista.
    :param locatie: string
    :param unde_locatie: string
    :param lista: list
    :return: lista noua, cu modificarile aferente.
    """
    rez = []
    for obiect in lista:
        if getLocation(obiect) != locatie:
            rez.append(obiect)
        else:
            id = getId(obiect)
            nume = getName(obiect)
            descriere = getDescription(obiect)
            pret = getPrice(obiect)
            obiect = creeazaObiect(id, nume, descriere, pret, unde_locatie)
            rez.append(obiect)
    return rez
