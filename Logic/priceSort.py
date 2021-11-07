from Domain.obiect import getPrice


def sortPrices(lista):
    """
    Functia va sora crescator fiecare obiect in functie de pret.
    :param lista: lst
    :return: lista sortata
    """
    return sorted(lista, key=lambda obiect: getPrice(obiect))
