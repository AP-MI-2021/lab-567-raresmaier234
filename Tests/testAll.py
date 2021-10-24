from Tests.TestDomain import testObiect
from Tests.testCrud import testAddObject, testDeleteObject, testModifyObject


def runAllTests():
    testObiect()
    testAddObject()
    testDeleteObject()
    testModifyObject()
