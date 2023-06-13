import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.helpers.pythonmethods import HelperMethods
from features.helpers.selectors import Selectors


# This method will get the list of prices or names from the UI and then write it to the tempdata file as a JSON
@when('I note all the "{Filter}" in the homepage')
def NoteAllThePrices(context, Filter):
    match Filter:
        case "prices":
            Prices = context.driver.find_elements(By.CLASS_NAME, Selectors.PricesList)
            FormattedPrices = HelperMethods.ConvertPricesToFloat(Prices)
            PricesInDataFile = {"PriceList": FormattedPrices}
            HelperMethods.WriteToFile(PricesInDataFile, "features/helpers/tempdata.json")
        case "names":
            Names = context.driver.find_elements(By.CLASS_NAME, Selectors.ProductList)
            FormattedNames = HelperMethods.FormatNames(Names)
            NamesInDataFile = {"NamesList": FormattedNames}
            HelperMethods.WriteToFile(NamesInDataFile, "features/helpers/tempdata.json")
        case default:
            print(Filter + " not supported")


# This method will select a sort option from a dropdown
@when('I select the "{SortOption}" sort option')
def SelectTheSortOption(context, SortOption):
    element = Select(context.driver.find_element(By.CLASS_NAME, Selectors.SortOption))
    element.select_by_visible_text(SortOption)


# This method will confirm whether a sort is correct in the UI or not
# It first will get all the sorted prices/names from the UI and puts them in a list (List A) after formatting them
# Then it will read the unsorted prices/names from the tempdata file and sort them using Python's sorted method
# Then puts them into a list (List B)
# Finally it compares if List A is the same as List B
@then('I confirm that the "{SortOption}" sort is correct')
def SortIsCorrect(context, SortOption):
    match SortOption:
        case "Price (high to low)":
            # Get sorted prices from UI and keep them in FormattedPricesInUI after formatting
            Prices = context.driver.find_elements(By.CLASS_NAME, Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices)

            # Get unsorted prices from tempdata and then sort them using sorted()
            # and keep them in FormattedPricesAfterSort
            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort, reverse=True)

            # Compare if both are same
            assert FormattedPricesInUI == FormattedPricesAfterSort

        case "Price (low to high)":
            Prices = context.driver.find_elements(By.CLASS_NAME, Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices)

            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort)

            assert FormattedPricesInUI == FormattedPricesAfterSort

        case "Name (Z to A)":
            Names = context.driver.find_elements(By.CLASS_NAME, Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names)

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort, reverse=True)

            assert NamesFromUI == NamesFromDataFileAfterSort

        case "Name (A to Z)":
            Names = context.driver.find_elements(By.CLASS_NAME, Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names)

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort)

            assert NamesFromUI == NamesFromDataFileAfterSort

        case default:
            print(SortOption + " not supported")


# This method adds a product to the cart. It gets all the names of the product and calls a helper method which puts the
# names in a list. Then gets the index of the product from the feature file and then clicks on it.
@when('I add "{Product}" to the cart')
def SelectTheProduct(context, Product):
    Names = context.driver.find_elements(By.CLASS_NAME, Selectors.ProductList)
    NamesFromUI = HelperMethods.FormatNames(Names)

    Index = NamesFromUI.index(Product)
    context.driver.find_elements(By.CLASS_NAME, Selectors.AddToCartButton)[Index].click()


# This method confirms the number of products in the cart
@when('I confirm that the cart has "{Number}" products')
def ConfirmNumberInCart(context, Number):
    assert context.driver.find_element(By.CLASS_NAME, Selectors.CartNumber).text == Number


# This method removes a product from the cart. It gets all the names of the product and calls a helper method which
# puts the names in a list. Then gets the index of the product from the feature file and then clicks on it.
@when('I remove "{Product}" from the cart')
def RemoveTheProduct(context, Product):
    Names = context.driver.find_elements(By.CLASS_NAME, Selectors.ProductList)
    NamesFromUI = HelperMethods.FormatNames(Names)

    Index = NamesFromUI.index(Product)
    context.driver.find_elements(By.CLASS_NAME, Selectors.RemoveFromCartButton)[Index].click()
