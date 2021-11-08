from Logic.CRUD import addObject


def test_UndoRedo():
    lista = []
    undo_list = []
    redo_list = []

    rez = addObject("1", "masina", "jucarie", 230, "cora", lista)
    undo_list.append(rez)
    lista = rez

    assert len(undo_list) == 1
    assert len(redo_list) == 0