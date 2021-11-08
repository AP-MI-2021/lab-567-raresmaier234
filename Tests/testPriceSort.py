from Domain.obiect import getPrice
from Logic.CRUD import addObject
from Logic.priceSort import sortPrices


def test_PriceSort():
    lista = []
    lista = addObject("1", "masina", "jucarie", 100, "toys", lista)
    lista = addObject("2", "pix", "albastru", 4, "lidl", lista)
    lista = addObject("3", "casca", "mtb", 200, "dhs", lista)

    rezultat = sortPrices(lista)
    assert getPrice(rezultat[0]) == 4
    assert getPrice(rezultat[1]) == 100
    assert getPrice(rezultat[2]) == 200


