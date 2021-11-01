from Domain.obiect import getLocation, getPrice
from Logic.CRUD import getByLocation


def listLocation(lista):
    """
    Functia va adauga in lista de locatii fiecare locatie care nu apartine acesteia, o singura data.
    :param lista: list
    :return: va returna lista de locatii.
    """
    listLocation = []
    for obiect in lista:
        if getLocation(obiect) not in listLocation:
            listLocation.append(getLocation(obiect))
    return listLocation


def maxObjectPrice(lista):
    """
    Functia va afla pretul maxim al fiecarei locatii din lista de locatii.
    :param lista: list
    :return: lista de sume maxime per fiecare locatie
    """
    locations = listLocation(lista)
    listOfMaxSums = []
    for location in locations:
        maxim = 0
        for obiect in lista:
            if getLocation(obiect) == location and getPrice(obiect) > maxim:
                maxim = getPrice(obiect)
        listOfMaxSums.append(maxim)
    return listOfMaxSums

