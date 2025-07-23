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
    wait = WebDriverWait(driver, 20)
    #Relative XPath for email field validation
    email_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[1]/p"
    )))

    #Relative XPath for password field validation
    password_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/p"
    )))
    assert email_error.text.strip() == "Email is required", "Email validation failed"
    assert password_error.text.strip() == "Password is required", "Password validation failed"
    print("Blank fields error shown")

def test_blank_email(driver):
    signinPage(driver).login("", "Insurance@123")
    wait = WebDriverWait(driver, 20)
    #Relative XPath for email field validation
    email_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[1]/p"
    )))
    assert email_error.text.strip() == "Email is required", "Email validation failed"
    print("Blank email error shown")

def test_blank_password(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "")
    wait = WebDriverWait(driver, 20)
    #Relative XPath for password field validation
    password_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/p"
    )))
    assert password_error.text.strip() == "Password is required", "Password validation failed"
    print("Blank password error shown")

def test_invalid_email_format(driver):
    signinPage(driver).login("invalid-email", "Insurance@123")
    wait = WebDriverWait(driver, 20)
    #Relative XPath for password field validation
    email_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[1]/p"
    )))
    assert email_error.text.strip() == "Please Enter Valid Email", "Invalid email validation failed"
    print("Invalid email format error shown")

def test_short_password(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "Test@12")
    wait = WebDriverWait(driver, 20)
    #Relative XPath for password field validation
    password_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/p"
    )))
    assert password_error.text.strip() == "password must be at least 8 characters", "Invalid password validation failed"
    print("Short password error shown")

def test_invalid_password_format(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "test12")
    wait = WebDriverWait(driver, 20)
    password_error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/p"
    )))
    assert password_error.text.strip() == "Must include at least one digit, one uppercase letter, one lowercase letter, one special character, and no white space", "Invalid password validation failed"
    print("Short password error shown")

def test_temporary_inactive_user(driver):
    signinPage(driver).login("kishang@gmail.com", "Test@123")
    wait = WebDriverWait(driver, 20)
    account_inactive = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'You are temporarily inactive, please contact support.')]")))
    assert "You are temporarily inactive, please contact support." in account_inactive.text
    print("Temporarily inactive User")

def test_terminate_user(driver):
    signinPage(driver).login("klcrkamalsharma@gmail.com", "Test@123")
    wait = WebDriverWait(driver, 20)
    terminate_user = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Account not found.')]")))
    assert "Account not found." in terminate_user.text
    print("Terminate User")

def test_resigned_user(driver):
    signinPage(driver).login("klcrrajnishbajpai@gmail.com", "Test@123")
    wait = WebDriverWait(driver, 20)
    resigned_user = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Account not found.')]")))
    assert "Account not found." in resigned_user.text
    print("Resigned User")