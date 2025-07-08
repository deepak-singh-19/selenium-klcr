from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_company_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Company
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[6]/button').click()
    # time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[7]/div[2]/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/button[2]').click()
    time.sleep(2)

    # Assert that the company page is open
    assert "company" in driver.current_url.lower()
    print("Company opened successfully")
