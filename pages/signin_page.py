import pytest
from selenium.webdriver.common.by import By

class signinPage:
    def __init__(self, driver):
        self.driver = (driver)
    def login(self, username, password):
        self.driver.get("http://67.205.148.222/insurance/app/auth/signin/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/div[1]/div/input').send_keys(username)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/button').click()
