from Domain.obiect import getLocation, getPrice, getDescription, getName, getId
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
        if getLocation(obiect) == locatie:
            locatie = unde_locatie
            if len(locatie) > 4:
                raise ValueError("Noua locatie trebuie sa aibe cel mult 4 caractere!")
            rez = modifyObject(getId(obiect), getName(obiect), getDescription(obiect), getPrice(obiect), locatie, lista)
        else:
            rez = obiect
    return rez
