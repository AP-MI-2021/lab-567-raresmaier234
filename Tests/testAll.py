from Tests.TestDomain import testObiect
from Tests.testConcatenate import test_concatenateDescription
from Tests.testCrud import testAddObject, testDeleteObject, testModifyObject
from Tests.testMaxObjPrice import test_listLocation, test_maxObjectPrice
from Tests.testMoveObject import testMoveObject
from Tests.testPriceSort import test_PriceSort
from Tests.testSumPrices import test_SumPrices
from Tests.testUndoRedo import test_UndoRedo


def runAllTests():
    testObiect()
    testAddObject()
    testDeleteObject()
    testModifyObject()
    testMoveObject()
    test_listLocation()
    test_maxObjectPrice()
    test_concatenateDescription()
    test_PriceSort()
    test_SumPrices()
    test_UndoRedo()