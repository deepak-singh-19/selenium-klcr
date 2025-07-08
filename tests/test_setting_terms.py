from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_terms_condition_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # setting > Terms & Conditions
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[8]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[9]/div/div/div/div[4]/div[2]/span').click()
    time.sleep(2)

    # Assert that the terms & conditions page is open
    assert "terms-conditions" in driver.current_url.lower()
    print("Terms Conditions opened successfully")
