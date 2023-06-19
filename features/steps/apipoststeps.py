import requests
from behave import *

from features.helpers.pythonmethods import HelperMethods


# This method makes a POST call to specific endpoints and then stores the response data in a tempfile
@given('I make a POST call to the "{APIEndpoint}" endpoint')
def IMakeAPostCall(context, APIEndpoint):
    match APIEndpoint:
        case "All products":
            RequestData = requests.post("https://automationexercise.com/api/productsList")
        case "Search product":
            for row in context.table:
                RequestData = requests.post("https://automationexercise.com/api/searchProduct",
                                            data={'search_product': row['Product']})
        case "Search product no param":
            for row in context.table:
                RequestData = requests.post("https://automationexercise.com/api/searchProduct")
        case "Login no email":
            RequestData = requests.post("https://automationexercise.com/api/verifyLogin")

    JsonData = RequestData.json()
    Data = {"Response": JsonData}
    HelperMethods.WriteToFile(Data, "features/helpers/tempData.json")


# This method will verify if 405 response is returned
@then('I verify that the method is not supported')
def IVerifyTheMethodIsNotSupported(context):
    Data = HelperMethods.ReadFromFile("features/helpers/tempData.json")

    ResponseCode = Data["Response"]["responseCode"]
    ResponseBody = Data["Response"]["message"]

    assert ResponseCode == 405
    assert ResponseBody == "This request method is not supported."


# This method will verify if the Search Product API returns the correct data
@then('I verify if I get the correct search result with "{ProductSearch}"')
def IVerifyIfIGetTheCorrectResult(context, ProductSearch):
    Data = HelperMethods.ReadFromFile("features/helpers/tempData.json")

    ResponseCode = Data["Response"]["responseCode"]
    ResponseBody = Data["Response"]["products"]

    assert ResponseCode == 200
    assert ProductSearch == ResponseBody[0]['name']


# This method will verify if 400 response is returned
@then('I verify that I get a Bad request response')
def IVerifyIfIGetABadReponse(context):
    Data = HelperMethods.ReadFromFile("features/helpers/tempData.json")

    ResponseCode = Data["Response"]["responseCode"]
    ResponseBody = Data["Response"]["message"]

    assert ResponseCode == 400
    assert "Bad request" in ResponseBody
    assert "parameter is missing in POST request" in ResponseBody
