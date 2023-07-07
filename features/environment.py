# This is the environment.py file. This hosts all the drivers and includes the before and after methods.

import geckodriver_autoinstaller
from selenium import webdriver
import chromedriver_autoinstaller
import edgedriver_autoinstaller
from features.helpers.pythonmethods import HelperMethods
from features.helpers.seleniummethods import ResetAppState


# This is the before, this method is executed before all the tests, so we are initializing the driver here
# It uses the auto installer, so no need to specify a driver directly
def before_all(context):
    chromedriver_autoinstaller.install()
    context.driver = webdriver.Chrome()

    # edgedriver_autoinstaller.install()
    # context.driver = webdriver.Edge()

    context.driver.implicitly_wait(10)


# This is the after, this method is executed after all the tests, so we are closing the the driver
# here. If we have any cleanup methods, put it above driver quit method.
def after_all(context):
    HelperMethods.ClearTempData()
    context.driver.quit()


# This is the before tag method. This will be executed before the specified tag is run
def before_tag(context, tag):
    if tag == "cleanappstate":
        ResetAppState(context)


# This is the after scenario method. It runs after every scenario, its used to take screenshots and attach to the report
def after_scenario(context, scenario):
    def ScreenshotData(mime_type, data, title):
        non_empty_data = " " if not data else data
        for formatter in context._runner.formatters:
            if "html" in formatter.name:
                formatter.embed(mime_type=mime_type, data=non_empty_data)
                return
    context.embed = ScreenshotData

    Screenshot = context.driver.get_screenshot_as_base64()
    context.embed(mime_type="image/png", data=Screenshot, title="Screenshot")
