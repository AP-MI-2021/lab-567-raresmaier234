from Domain.obiect import getLocation, getPrice, getDescription, getName, getId


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
    newList = []
    for obiect in lista:
        if getLocation(obiect) == locatie:
            newLocation = unde_locatie
            if len(newLocation) > 4:
                raise ValueError("Noua locatie trebuie sa aibe cel mult 4 caractere!")
            obiect[4] = newLocation
            newList.append(obiect)
        else:
            newList.append(obiect)
    return newList
