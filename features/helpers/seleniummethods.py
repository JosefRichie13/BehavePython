# This file will contain all the helper methods which are related to selenium

import json

from selenium.webdriver.common.by import By

# This method returns False when an element is not found
def ElementNotDisplayed(context, element):
    try:
        assert context.driver.find_element(By.CLASS_NAME, element).is_displayed() == True
    except:
        return False
