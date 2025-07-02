from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By


def test_open_designation_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    #signin.login("info@klcrinvestigations.com", "Insurance@123") #- Staging server
    signin.login("superadmin@insurance.com", "Insurance@123") # 67 server

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    #Click System -> User
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[5]/div[2]/span').click()
    time.sleep(2)

    # Assert that the designation page is open
    assert "designation" in driver.current_url.lower()
    print("Designation Type page opened successfully")

