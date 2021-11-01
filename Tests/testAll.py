from Tests.TestDomain import testObiect
from Tests.testCrud import testAddObject, testDeleteObject, testModifyObject
from Tests.testMaxObjPrice import test_listLocation, test_maxObjectPrice
from Tests.testMoveObject import testMoveObject


def runAllTests():
    testObiect()
    testAddObject()
    testDeleteObject()
    testModifyObject()
    testMoveObject()
    test_listLocation()
    test_maxObjectPrice()