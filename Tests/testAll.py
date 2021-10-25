from Tests.TestDomain import testObiect
from Tests.testCrud import testAddObject, testDeleteObject, testModifyObject
from Tests.testMoveObject import testMoveObject


def runAllTests():
    testObiect()
    testAddObject()
    testDeleteObject()
    testModifyObject()