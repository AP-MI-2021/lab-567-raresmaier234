from Logic.CRUD import addObject


def test_UndoRedo():
    lista = []
    undo_list = []
    redo_list = []

    lista = addObject("11", "masina", "jucarie", 230, "cora", lista)
    undo_list.append(lista)
    lista = addObject("22", "carte", "bucate", 50, "lidl", lista)
    undo_list.append(lista)
    lista = addObject("33", "carti", "joc", 25, "toys", lista)
    undo_list.append(lista)
    assert len(undo_list) == 3
    undo_list.pop()
    redo_list.append(lista)
    assert len(undo_list) == 2
    undo_list.pop()
    redo_list.append(lista)
    assert len(undo_list) == 1
    undo_list.pop()
    redo_list.append(lista)
    assert len(undo_list) == 0
    assert len(redo_list) == 3

    redo_list = []
    lista = addObject("1", "masina", "jucarie", 230, "cora", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = addObject("2", "carte", "bucate", 50, "lidl", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = addObject("3", "carti", "joc", 25, "toys", lista)
    undo_list.append(lista)
    redo_list.clear()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    undo_list.pop()
    redo_list.append(lista)
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    undo_list.pop()
    redo_list.append(lista)
    assert len(redo_list) == 2
    assert len(undo_list) == 1

    redo_list.pop()
    undo_list.append(lista)
    assert len(redo_list) == 1
    assert len(undo_list) == 2

    redo_list.pop()
    undo_list.append(lista)
    assert len(redo_list) == 0
    assert len(undo_list) == 3

    undo_list.pop()
    redo_list.append(lista)
    assert len(redo_list) == 1
    assert len(undo_list) == 2

    lista = addObject("4", "masina", "jucarie", 33, "toys", lista)
    undo_list.append(lista)
    redo_list.clear()
    assert len(redo_list) == 0
    assert len(undo_list) == 3

    undo_list.pop()
    redo_list.append(lista)
    assert len(undo_list) == 2
    assert len(redo_list) == 1

    undo_list.pop()
    redo_list.append(lista)
    assert len(undo_list) == 1
    assert len(redo_list) == 2

    redo_list.pop()
    undo_list.append(lista)
    assert len(undo_list) == 2
    assert len(redo_list) == 1

    redo_list.pop()
    undo_list.append(lista)
    assert len(undo_list) == 3
    assert len(redo_list) == 0

    if len(redo_list) > 0:
        redo_list.pop()
    assert len(redo_list) == 0




