from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By


def test_open_user_type_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("superadmin@insurance.com", "Insurance@123")

    #Redirect to the user type page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[3]/div[2]/span').click()
    time.sleep(2)

    # Assert that the User Type page is open
    assert "user-type" in driver.current_url.lower()
    print("User Type page opened successfully")

