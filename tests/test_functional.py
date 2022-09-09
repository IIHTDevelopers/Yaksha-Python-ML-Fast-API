#import sys, os
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
import unittest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_root(self):
        test_obj = TestUtils()
        try:
            response = client.get("/")
            passed = response.status_code == 200
            if passed:
                test_obj.yakshaAssert("TestRoot",True,"boundary")
                print("TestRoot= Passed")
            else:
                test_obj.yakshaAssert("TestRoot",False,"boundary")
                print("TestRoot = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestRoot",False,"boundary")
            print("TestRoot = Failed")

        assert passed

    def test_create_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.post("/recipe", json = {"recipe" : "potato chips"})
            passed = response.status_code == 200
            #passed = response.json()["recipe"] == "potato chips"
            if passed:
                test_obj.yakshaAssert("TestCreateRecipe",True,"boundary")
                print("TestCreateRecipe = Passed")
            else:
                test_obj.yakshaAssert("TestCreateRecipe",False,"boundary")
                print("TestCreateRecipe = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestCreateRecipe",False,"boundary")
            print("TestCreateRecipe = Failed")
        assert passed

    def test_read_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.post("/recipe", json = {"recipe" : "potato chips"})
            passed = response.status_code == 200

            if passed:
                id = response.json()["id"]
                recipe = response.json()["recipe"]
                response = client.get("/recipe/"+str(id))
                passed = response.status_code == 200
                if passed:
                    passed = response.json() == {"id": id, "recipe": recipe}
            if passed:
                test_obj.yakshaAssert("TestReadRecipe",True,"boundary")
                print("TestReadRecipe = Passed")
            else:
                test_obj.yakshaAssert("TestReadRecipe",False,"boundary")
                print("TestReadRecipe= Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestReadRecipe",False,"boundary")
            print("TestReadRecipe = Failed")
        assert passed

    def test_update_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.post("/recipe", json = {"recipe" : "kadai chicken"})
            passed = response.status_code == 200
            if passed:
                id = response.json()["id"]
                response = client.put("/recipe/" + str(id) + "?recipe=chicken nuggets")
                passed = response.status_code == 200
                if passed:
                    id = response.json()["id"]
                    recipe = response.json()["recipe"]
                    passed = response.json() == {"id": id, "recipe": recipe}
            if passed:
                test_obj.yakshaAssert("TestUpdateRecipe",True,"boundary")
                print("TestUpdateRecipe = Passed")
            else:
                test_obj.yakshaAssert("TestUpdateRecipe",False,"boundary")
                print("TestUpdateRecipe = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestUpdateRecipe",False,"boundary")
            print("TestUpdateRecipe = Failed")
        assert passed

    def test_delete_recipe(self):
        test_obj = TestUtils()
        try:
            response = client.post("/recipe", json = {"recipe" : "kadai chicken"})
            passed = response.status_code == 200
            if passed:
                id = response.json()["id"]
                response = client.delete("/recipe/" + str(id))
                passed = response.status_code == 200
                if passed:
                    response = client.get("/recipe/"+str(id))
                    passed = response.status_code == 410
            if passed:
                test_obj.yakshaAssert("TestDeleteRecipe",True,"boundary")
                print("TestDeleteRecipe = Passed")
            else:
                test_obj.yakshaAssert("TestDeleteRecipe",False,"boundary")
                print("TestDeleteRecipe = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestDeleteRecipe",False,"boundary")
            print("TestDeleteRecipe = Failed")
        assert passed
