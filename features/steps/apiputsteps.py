import requests
from behave import *

from features.helpers.pythonmethods import HelperMethods


# This method makes a PUT call to specific endpoints and then stores the response data in a tempfile
@given('I make a PUT call to the "{APIEndpoint}" endpoint')
def IMakeAPostCall(context, APIEndpoint):
    match APIEndpoint:
        case "All brands":
            RequestData = requests.put("https://automationexercise.com/api/brandsList")

    JsonData = RequestData.json()
    Data = {"Response": JsonData}
    HelperMethods.WriteToFile(Data, "features/helpers/tempData.json")
