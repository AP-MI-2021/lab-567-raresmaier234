from Logic.CRUD import addObject
from Tests.testAll import runAllTests
from UI.command import menu
from UI.console import runUI


def main():
    runAllTests()
    lista = []
    runUI(lista)


if __name__ == '__main__':
    main()
