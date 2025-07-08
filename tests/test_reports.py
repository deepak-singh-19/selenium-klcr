from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_reports_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # setting > Reports
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[8]/button').click()
    # time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[9]/div[2]/span').click()
    time.sleep(2)

    # Assert that the Reports page is open
    assert "case-report" in driver.current_url.lower()
    print("Case Report opened successfully")
