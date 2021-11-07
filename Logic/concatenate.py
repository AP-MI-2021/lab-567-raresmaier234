from Domain.obiect import creeazaObiect, getName, getId, getDescription, getPrice, getLocation


def concatenateDescription (lista, pret, descriere):
    """
    Functia va concatena descrierea, cu o alta descriere data de utilizator ulterior, in cazul in care
    valoarea data de utilizator este mai mare decat pretul obiectului.
    :param lista: lst
    :param pret: float
    :param descriere: str
    :return: va returna noua lista, cu concatenarile aferente.
    """
    rezultat = []
    for obiect in lista:
        if getPrice(obiect) < pret:
            rezultat.append(creeazaObiect(getId(obiect), getName(obiect), getDescription(obiect) + descriere,
                                            getPrice(obiect), getLocation(obiect)))
        else:
            rezultat.append(creeazaObiect(getId(obiect), getName(obiect), getDescription(obiect), getPrice(obiect),
                                          getLocation(obiect)))
    return rezultat
