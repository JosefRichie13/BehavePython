import requests
from behave import *

from features.helpers.pythonmethods import HelperMethods


# This method makes a DELETE call to specific endpoints and then stores the response data in a tempfile
@given('I make a DELETE call to the "{APIEndpoint}" endpoint')
def IMakeAPostCall(context, APIEndpoint):
    match APIEndpoint:
        case "Verify login":
            RequestData = requests.put("https://automationexercise.com/api/verifyLogin")

    JsonData = RequestData.json()
    Data = {"Response": JsonData}
    HelperMethods.WriteToFile(Data, "features/helpers/tempData.json")
