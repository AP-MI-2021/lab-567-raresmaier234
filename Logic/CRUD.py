from Domain.obiect import creeazaObiect, getId, getLocation


def addObject(id, nume, descriere, pret, locatie, lista):
    """
    Adauga in lista un obiect nou
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: lista cu toate obiectele din depozit, dupa adaugare
    """
    obiect = creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def getById(id, lista):
    """
    Va cauta in lista, obiectul dat de utilizator in functie de id
    :param id: string
    :param lista: list
    :return: obiectul in functie de id-ul dat de utilizator, din lista
    """
    for obiect in lista:
        if getId(obiect) == id:
            return obiect


def getByLocation(location, lista):
    """

    :param location:
    :param lista:
    :return:
    """
    for obiect in lista:
        if getLocation(obiect) == location:
            return obiect


def deleteObject(id, lista):
    """
    Va sterge obiectul cu id-ul dat de utilizator din lista.
    :param id: string
    :param lista: list
    :return: lista de obiecte dupa sterge
    """
    return [obiect for obiect in lista if getId(obiect) != id]


def modifyObject(id, nume, descriere, pret, locatie, lista):
    """
    Va modifica obiectul cu id-ul dat de utilizator
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: Va returna lista noua dupa modificari
    """
    listaNoua = []
    for obiect in lista:
        if getId(obiect) == id:
            obiectNou = creeazaObiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua


