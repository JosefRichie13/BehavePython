# This file will contain all the helper methods which are related to selenium

from features.helpers.configs import Configs
from features.helpers.selectors import Selectors
from selenium.webdriver.common.by import By


# This method returns False when an element is not found
def ElementNotDisplayed(context, element):
    try:
        assert context.driver.find_element(By.CLASS_NAME, element).is_displayed() == True
    except:
        return False


# This method will reset the app to the original state.
def ResetAppState(context):
    context.driver.get(Configs.MainURL)
    context.driver.find_element(By.ID, Selectors.UserName).send_keys(Configs.ValidUser)
    context.driver.find_element(By.ID, Selectors.Password).send_keys(Configs.Password)
    context.driver.find_element(By.ID, Selectors.LoginButton).click()
    context.driver.find_element(By.ID, Selectors.Menu).click()
    context.driver.find_element(By.ID, Selectors.ResetApp).click()
