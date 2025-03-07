import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
email="email"
password="password"

class loginclass:
    def __init__(self,driver):
        self.driver=driver
    def login(self):
        self.driver.find_element(By.ID,email).send_keys("admin@admin.com")
        time.sleep(4)
        self.driver.find_element(By.ID, password).send_keys("Welcome@l1")
        time.sleep(4)
        # self.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/form/div[3]/button').click()
        # time.sleep(2)



