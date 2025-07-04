from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
import time


def test_open_employment_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    #Click System -> User
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[2]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[4]/div[2]/span').click()
    time.sleep(2)

    # Assert that the User page is open
    assert "employment-type" in driver.current_url.lower()
    print("Employment Type page opened successfully")