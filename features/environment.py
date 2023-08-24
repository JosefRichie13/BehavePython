# This is the environment.py file. This hosts all the drivers and includes the before and after methods.

from selenium import webdriver
import geckodriver_autoinstaller
import chromedriver_autoinstaller
import edgedriver_autoinstaller

from features.helpers.pythonmethods import HelperMethods
from features.helpers.seleniummethods import ResetAppState

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# This is the before, this method is executed before all the tests, so we are initializing the driver here
# It uses the auto installer, so no need to specify a driver directly
def before_all(context):

    # New Selenium Webdriver Manager
    #context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # Headless mode
    # BrowserOptions = webdriver.ChromeOptions()
    # BrowserOptions.add_argument("--headless=new")
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=BrowserOptions)

    # Old auto installer drivers
    #chromedriver_autoinstaller.install()
    #edgedriver_autoinstaller.install()
    #context.driver = webdriver.Edge()

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
