from Domain.obiect import getLocation, getPrice
from Logic.CRUD import getByLocation


def listLocation(lista):
    listLocation = []
    for obiect in lista:
        if getLocation(obiect) not in listLocation:
            listLocation.append(getLocation(obiect))
    return listLocation


def maxObjectPrice(lista):
    locations = listLocation(lista)
    listOfMaxSums = []
    for location in locations:
        maxim = 0
        for obiect in lista:
            if getLocation(obiect) == location and getPrice(obiect) > maxim:
                maxim = getPrice(obiect)
        listOfMaxSums.append(maxim)
    return listOfMaxSums

