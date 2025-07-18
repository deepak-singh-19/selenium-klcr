from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By


def test_open_user_type_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    #Click Master -> Doctor
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/button').click()
    time.sleep(1)

    #---Open the doctor page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[4]/div/div/div/div[8]/div[2]/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]').click()
    time.sleep(5)

    # Assert that the User Type page is open
    assert "doctors" in driver.current_url.lower()
    print("Doctors page opened successfully")

