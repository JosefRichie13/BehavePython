from behave import *
from selenium.webdriver.common.by import By

from features.helpers.selectors import Selectors


# This method clicks on the cart
@when('I click on the cart')
def ClickOnTheCart(context):
    context.driver.find_element(By.CLASS_NAME, Selectors.Cart).click()


# This method clicks on the checkout
@when('I checkout')
def ICheckout(context):
    context.driver.find_element(By.ID, Selectors.Checkout).click()


# This method enters the information in the checkout page. It uses a DataTable. Then it proceeds from the page
@when('I enter my information to continue')
def IEnterMyInformation(context):
    for row in context.table:
        context.driver.find_element(By.ID, Selectors.FirstName).send_keys(row['FirstName'])
        context.driver.find_element(By.ID, Selectors.LastName).send_keys(row['LastName'])
        context.driver.find_element(By.ID, Selectors.ZipCode).send_keys(row['Zip'])

    context.driver.find_element(By.ID, Selectors.ContinueButton).click()


# This method clicks on the order confirmation
@when('I confirm my order')
def IConfirmTheOrder(context):
    context.driver.find_element(By.ID, Selectors.FinishButton).click()


# This method verifies if we can see the correct message in the checkout screen
@then('I should see "{Message}" after the order is placed')
def SeeTheMessageAfterOrder(context, Message):
    assert context.driver.find_element(By.CLASS_NAME, Selectors.CheckoutBanner).text == Message
