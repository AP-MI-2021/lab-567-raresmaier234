from Logic.CRUD import addObject
from Logic.sumPrices import sumPrices


def test_SumPrices():
    lista = []
    lista = addObject("1", "masina", "jucarie", 100, "toys", lista)
    lista = addObject("2", "pix", "albastru", 4, "lidl", lista)
    lista = addObject("3", "casca", "mtb", 200, "toys", lista)
    lista = addObject("4", "telefon", "mobil", 4000, "shop", lista)

    rez = sumPrices(lista)
    assert rez["toys"] == 300
    assert rez["lidl"] == 4
    assert rez["shop"] == 4000
