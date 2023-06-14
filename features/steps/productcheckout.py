from behave import *
from selenium.webdriver.common.by import By
import re
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

# This method calculates Tax at 8% and verifies it its applied
# It first gets the non taxed total price from the UI and removes all the $ symbols.
# Then it multiplies it by 0.08 and rounds it to 2 decimals, giving us the 8% tax rate
# Then the non taxed price and the tax rate are added
# Finally it gets the taxed total price from the UI and removed all the $ symbol
# Then asserts if the prices from the UI and the calculated price are the same
@then('I confirm that the tax is calculated at 8 percent')
def TaxCalculation(context):
    PriceBeforeTax = context.driver.find_element(By.CLASS_NAME, Selectors.TotalPriceBeforeTax).text
    OnlyPriceBeforeTax = re.findall("\d+\.\d+", PriceBeforeTax)[0]
    TaxAdded = 0.08 * float(OnlyPriceBeforeTax)
    RoundedTaxAdded = round(TaxAdded, 2)
    PriceAfterTax = float(OnlyPriceBeforeTax) + float(RoundedTaxAdded)

    PriceAfterTaxFromUI = context.driver.find_element(By.CLASS_NAME, Selectors.TotalPriceAfterTax).text
    OnlyPriceAfterTaxFromUI = re.findall("\d+\.\d+", PriceAfterTaxFromUI)[0]

    assert PriceAfterTax == float(OnlyPriceAfterTaxFromUI)

