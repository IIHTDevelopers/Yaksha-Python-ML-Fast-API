import unittest
from fastapi.testclient import TestClient
from main import app
#import sys, os
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'

client = TestClient(app)
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_get_recipe_id_string(self):
        test_obj = TestUtils()
        try:
            response = client.get("/recipe/abc")
            passed = response.status_code == 422
            passed = response.json()["detail"][0]["msg"] == "value is not a valid integer"

            if passed:
                test_obj.yakshaAssert("TestGetRecipeIdString",True,"boundary")
                print("TestGetRecipeIdString = Passed")
            else:
                test_obj.yakshaAssert("TestGetRecipeIdString",False,"boundary")
                print("TestGetRecipeIdString = Failed")

        except:
            passed = False
            test_obj.yakshaAssert("TestGetRecipeIdString",False,"boundary")
            print("TestGetRecipeIdString = Failed")
        assert passed

    def test_read_NA_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.get("/recipe/"+str(999999232399923))
            passed = response.status_code == 410

            if passed:
                test_obj.yakshaAssert("TestReadNArecipe",True,"boundary")
                print("TestReadNArecipe = Passed")
            else:
                test_obj.yakshaAssert("TestReadNArecipe",False,"boundary")
                print("TestReadNArecipe = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestReadNArecipe",False,"boundary")
            print("TestReadNArecipe = Failed")
        assert passed

    def test_update_NA_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.put("/recipe/" + str(999999232399923) + "?recipe=chicken nuggets")
            passed = response.status_code == 410
            if passed:
                test_obj.yakshaAssert("TestUpdateNArecipe",True,"boundary")
                print("TestUpdateNArecipe = Passed")
            else:
                test_obj.yakshaAssert("TestUpdateNArecipe",False,"boundary")
                print("TestUpdateNArecipe = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestUpdateNArecipe",False,"boundary")
            print("TestUpdateNArecipe" = Failed")
        assert passed
