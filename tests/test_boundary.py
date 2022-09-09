
#import sys, os
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_boundary_revised.txt'
import unittest
from test.TestUtils import TestUtils
class BoundaryTest(unittest.TestCase):
    def test_dummy_boundary_testcase(self):
        test_obj = TestUtils()
        try:
            test_obj.yakshaAssert("TestDummyBoundaryTestCase",True,"boundary")
            print("TestDummyBoundaryTestCase = Passed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestDummyBoundaryTestCase",False,"boundary")
            print("TestDummyBoundaryTestCase = Failed")
