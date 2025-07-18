import faker.providers.date_time

from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

def generate_random_doctor_data():
    fake = Faker('en_In')
    data = {
        "name": fake.name(),
        "registration_number": fake.random_number()[:10],
        "contact_number": fake.msisdn()[:10],
        "address": fake.address(),
        "clinic_address": fake.address(),
    }
    return data

def ensure_drawer_expanded(driver, wait):
    """
    Ensures the left-hand drawer/sidebar is expanded.
    Idempotent: does nothing if already expanded and 'System' is visible.
    """
    MASTER_XPATH = '//*[@id=":r5:"]'
    DRAWER_TOGGLE_XPATH = '//*[@id=":r3:"]'
    # If the "System" link is not visible, the drawer is probably collapsed.
    if not driver.find_elements(By.XPATH, MASTER_XPATH):
        try:
            toggle = wait.until(EC.element_to_be_clickable((By.XPATH, DRAWER_TOGGLE_XPATH)))
            toggle.click()
            wait.until(EC.visibility_of_element_located((By.XPATH, MASTER_XPATH)))
        except Exception as e:
            print("Failed to auto-expand drawer:", str(e))
            # Optionally: assert False, "Drawer auto-expand failed"

def test_open_user_type_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    # time.sleep(2)

    #Click Master -> Doctor
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/button').click()
    time.sleep(1)

    #---Open the doctor page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[4]/div/div/div/div[8]/div[2]/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]').click()
    time.sleep(5)

    #------fill doctor page with random data
    user_data = generate_random_doctor_data()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[1]/div/div/input').send_keys(user_data['name'])
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id=":r39:"]').send_keys(user_data['registration_number'])
    time.sleep(3)


    # Assert that the User Type page is open
    assert "doctors" in driver.current_url.lower()
    print("Doctors page opened successfully")

