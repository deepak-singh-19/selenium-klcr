from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_credit_notes_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click Accounts -> Credit noted
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[5]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[6]/div/div/div/div[4]/div[2]/span').click()
    time.sleep(2)

    # Assert that the report credit notes page is open
    assert "credit-notes" in driver.current_url.lower()
    print("Credit Notes Billing page opened successfully")
