from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_case_management_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click Claims -> Case Management
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[4]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[5]/div/div/div/div[1]/div[2]/span').click()
    time.sleep(2)

    # Assert that the state page is open
    assert "case-management" in driver.current_url.lower()
    print("Case Management page opened successfully")
