# This is the environment.py file. This hosts all the drivers and includes the before and after methods.
import geckodriver_autoinstaller
from selenium import webdriver
import chromedriver_autoinstaller
import edgedriver_autoinstaller
from features.helpers.pythonmethods import HelperMethods


def before_all(context):
    # This is the before, this method is executed before all the tests, so we are initializing the driver here
    # It uses the auto installer, so no need to specify a driver directly

    chromedriver_autoinstaller.install()
    context.driver = webdriver.Chrome()

    #edgedriver_autoinstaller.install()
    #context.driver = webdriver.Edge()

    context.driver.implicitly_wait(10)


def after_all(context):
    # This is the after, this method is executed after all the tests, so we are closing the the driver
    # here. If we have any cleanup methods, put it above driver quit method.
    HelperMethods.ClearTempData()
    context.driver.quit()
