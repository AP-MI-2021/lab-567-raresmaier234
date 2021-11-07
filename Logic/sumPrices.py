from Domain.obiect import getLocation, getPrice


def sumPrices(lista):
    """
    Functia va cauta in lista locatiile care nu fac parte din tuplu "rez" si va adauga in
    rez pretul inital al obiectului, daca exista in rez locatia obiectului, va aduna la rez, pretul altui obiect din
    aceeasi locatie.
    :param lista: lst
    :return: suma totala per fiecare locatie.
    """
    rez = {}
    for obiect in lista:
        price = getPrice(obiect)
        location = getLocation(obiect)
        if location in rez:
            rez[location] += price
        else:
            rez[location] = price
    return rez
