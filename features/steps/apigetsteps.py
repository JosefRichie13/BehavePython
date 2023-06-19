import requests
from behave import *

from features.helpers.pythonmethods import HelperMethods


# This method makes a GET call to specific endpoints and then stores the response data in a tempfile
@given('I make a GET call to the "{APIEndpoint}" endpoint')
def IMakeAGetCall(context, APIEndpoint):
    match APIEndpoint:
        case "All products":
            RequestData = requests.get("https://automationexercise.com/api/productsList")

        case "All brands":
            RequestData = requests.get("https://automationexercise.com/api/brandsList")

    JsonData = RequestData.json()
    Data = {"Response": JsonData}
    HelperMethods.WriteToFile(Data, "features/helpers/tempData.json")


# This method will verify if All products API endpoint works correctly
@then('I verify that I get all the products are returned')
def IVerifyTheAllProductsEndpoint(context):
    Data = HelperMethods.ReadFromFile("features/helpers/tempData.json")

    ResponseCode = Data["Response"]["responseCode"]
    ResponseBody = Data["Response"]["products"]

    assert ResponseCode == 200
    assert len(ResponseBody) > 0


# This method will verify if All brands API endpoint works correctly
@then('I verify that all the brands are returned')
def IVerifyTheAllProductsEndpoint(context):
    Data = HelperMethods.ReadFromFile("features/helpers/tempData.json")

    ResponseCode = Data["Response"]["responseCode"]
    ResponseBody = Data["Response"]["brands"]

    assert ResponseCode == 200
    assert len(ResponseBody) > 0
