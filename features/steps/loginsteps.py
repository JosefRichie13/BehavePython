from behave import *
from selenium.webdriver.common.by import By

from features.helpers.configs import Configs
from features.helpers.selectors import Selectors
from features.helpers.seleniummethods import ElementNotDisplayed


# Opens the Webpage
@given('I open the web page')
def IOpenTheWebPage(context):
    context.driver.get(Configs.MainURL)


# Logs in as a specified user. Enters the corresponding username and password and clicks on the login button
@when('I login as a "{UserType}" user')
def ILoginAsAUser(context, UserType):
    match UserType:
        case "standard":
            context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.ValidUser)
            context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.Password)
        case "locked":
            context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.LockedUser)
            context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.Password)
        case "no_username":
            context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.Password)
        case "no_password":
            context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.ValidUser)
        case "wrong_username":
            context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.WrongUser)
            context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.Password)
        case "wrong_password":
            context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.ValidUser)
            context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.WrongUser)
        case default:
            print("Incorrect User Type")

    context.driver.find_element(By.ID, Selectors.LoginButton).click()


# Verifies the messages in the corresponding pages
@then('I should see "{Message}" in the "{Page}"')
def IShouldSeeTheHomePageMessage(context, Message, Page):
    match Page:
        case "homepage":
            assert context.driver.find_element(By.CLASS_NAME, Selectors.HomePageTitle).text == Message
            assert ElementNotDisplayed(context, Selectors.LoginButton) == False
        case "loginpage":
            assert context.driver.find_element(By.CLASS_NAME, Selectors.LoginPageTitle).text == Message
            assert context.driver.find_element(By.ID, Selectors.LoginButton).is_displayed() == True


# Verifies the error messages in the login page
@then('I should see the login error message "{Message}"')
def IShouldSeeTheLoginErrorMessage(context, Message):
    assert Message in context.driver.find_element(By.CLASS_NAME, Selectors.ErrorMessage).text


# Logs out of the webpage. It clicks on the hamburger menu, then on the logout button
@when('I Logout of the webpage')
def ILogoutOfTheWebPage(context):
    context.driver.find_element(By.ID, Selectors.Menu).click()
    context.driver.find_element(By.ID, Selectors.LogoutButton).click()
