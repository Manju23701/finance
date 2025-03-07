# # conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture
# def setup(request):
#     # Set up headless Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#
#     # Initialize the remote WebDriver pointing to your Selenium Grid Hub
#     driver = webdriver.Remote(
#         command_executor="http://192.168.1.58:4444/wd/hub",
#         options=chrome_options
#     )
#
#     # Attach the driver to the test class (so you can use self.driver)
#     request.cls.driver = driver
#
#     yield driver
#
#     # Teardown: quit the driver after tests complete
#     driver.quit()
#
#     @pytest.hookimpl(hookwrapper=True)
#     def pytest_runtest_makereport(item, call):
#         # Execute all other hooks to obtain the report object
#         outcome = yield
#         report = outcome.get_result()
#
#         # If the test failed
#         if report.when == "call" and report.failed:
#             driver_fixture = item.funcargs.get('driver', None)
#             if driver_fixture is not None:
#                 screenshot_file = f"{item.name}.png"
#                 driver_fixture.save_screenshot(screenshot_file)
# conftest.py
# conftest.py
# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the URL of your application under test.
# IMPORTANT: This should be the URL of the web app you want to test—not the Selenium Grid hub.
# For example, if your app is running locally on port 8000, then use:
APP_URL = "https://smiligencehr.itsfortesza.com/"
# If you intended to use a different port (e.g., 4440), update APP_URL accordingly.
# Note: Do NOT use the Grid Hub URL (e.g., "http://192.168.1.58:4444/wd/hub") here!

@pytest.fixture(scope="class")
def setup(request):
    # Configure headless Chrome options.
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the remote WebDriver that connects to the Selenium Grid Hub.
    # The Grid Hub URL (here "http://192.168.1.58:4444/wd/hub") is used for sending WebDriver commands.
    driver = webdriver.Remote(
        command_executor="http://192.168.1.58:4444/wd/hub",
        options=chrome_options
    )

    # Attach the driver to the test class so that tests can use self.driver.
    request.cls.driver = driver

    # Navigate to the application under test.
    driver.get(APP_URL)

    yield driver

    # Teardown: quit the driver after tests complete.
    driver.quit()


# This hook captures a screenshot if a test fails.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Here, we use the fixture name 'setup' to obtain the driver.
        driver = item.funcargs.get("setup", None)
        if driver is not None:
            screenshot_file = f"{item.name}.png"
            driver.save_screenshot(screenshot_file)
