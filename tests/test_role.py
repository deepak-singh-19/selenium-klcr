# tests/test_role.py
import pytest

from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
import time

def test_open_role_page(driver):
    signin = signinPage(driver)
    signin.login("superadmin@insurance.com", "Insurance@123")

    # Click on left drawer button
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click System -> Role
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[1]/div[2]/span').click()
    time.sleep(2)

    # Assert that the Role page is open
    assert "role" in driver.current_url.lower()
    print("Role page opened successfully")
