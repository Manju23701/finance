from selenium import webdriver
import pytest
@pytest.fixture(scope='function')
def setup(request):
    driver=webdriver.Chrome()
    url="http://192.168.1.57:8000/"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver

