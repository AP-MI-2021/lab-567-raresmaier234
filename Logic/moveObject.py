from Domain.obiect import getLocation, getPrice, getDescription, getName, getId


def moveObject(locatie, unde_locatie, lista):
    newList = []
    for obiect in lista:
        if getLocation(obiect) == locatie:
            newLocation = unde_locatie
            newList.append(
                {
                    "id": getId(obiect),
                    "nume": getName(obiect),
                    "descriere": getDescription(obiect),
                    "pret": getPrice(obiect),
                    "locatie": newLocation
                }
            )
        else:
            newList.append(obiect)
    return newList