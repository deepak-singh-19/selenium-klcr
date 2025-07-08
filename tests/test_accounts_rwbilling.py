from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_report_writer_billing_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click accounts -> Report writer Billings
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[5]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[6]/div/div/div/div[3]/div[2]/span').click()
    time.sleep(2)

    # Assert that the report writer billing page is open
    assert "report-writer-billing" in driver.current_url.lower()
    print("Report Writer Billing page opened successfully")
