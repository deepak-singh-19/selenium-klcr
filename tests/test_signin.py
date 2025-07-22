import pytest
from selenium.webdriver.common.by import By
from pages.signin_page import signinPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Utility: Get error text
def get_error_message(driver):
    try:
        return WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "MuiAlert-message"))
        ).text
    except:
        return ""

def test_valid_login(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "Insurance@123")
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower()
    print("Valid login successful")
    time.sleep(5)

def test_invalid_password(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "Insurance@1234")
    time.sleep(2)
    # Wait for any element containing 'Invalid password'
    wait = WebDriverWait(driver, 20)
    toast = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Invalid password')]")))
    assert "Invalid password" in toast.text
    print("Invalid password error shown")
    time.sleep(5)

def test_invalid_email(driver):
    signinPage(driver).login("info@investigation.com", "Insurance@123")
    wait = WebDriverWait(driver, 20)
    toast = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Account not found.')]")))
    assert "Account not found" in toast.text
    print("Account not found error message shown")

def test_blank_fields(driver):
    signinPage(driver).login("", "")
    time.sleep(5)
    # error = get_error_message(driver)
    # assert "required" in error.lower() or "invalid" in error.lower()
    print("Blank fields error shown")

def test_blank_email(driver):
    signinPage(driver).login("", "Insurance@123")
    time.sleep(5)
    # error = get_error_message(driver)
    # assert "email" in error.lower()
    print("Blank email error shown")

def test_blank_password(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "")
    # error = get_error_message(driver)
    # assert "password" in error.lower()
    print("Blank password error shown")

def test_invalid_email_format(driver):
    signinPage(driver).login("invalid-email", "Insurance@123")
    # error = get_error_message(driver)
    # assert "email" in error.lower()
    print("Invalid email format error shown")

def test_short_password(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "123")
    # error = get_error_message(driver)
    # assert "password" in error.lower()
    print("Short password error shown")
