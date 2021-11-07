from Domain.obiect import creeazaObiect, getId, getLocation, getPrice


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
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if len(locatie) != 4:
        raise ValueError("Acest id exista deja!")
    obiect = creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def getById(id, lista):
    """
    Va cauta in lista obiectul cu de id-ul dat de utilizator.
    :param id: string
    :param lista: list
    :return: obiectul in functie de id-ul dat de utilizator, din lista
    """
    for obiect in lista:
        if getId(obiect) == id:
            return obiect


def getByLocation(location, lista):
    """
    Va cauta in lista obiectul cu locatia data de utilizator.
    :param location: string
    :param lista: list
    :return: obiectul in functie de locatia data de utilizator
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
    if getById(id, lista) is None:
        raise ValueError("Obiectul pe care doresti sa-l stergi nu exista!")
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


