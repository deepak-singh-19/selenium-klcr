from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By
from faker import Faker
import random


# def generate_random_hospital_data():
#     fake = Faker('en_In')
#     state = ['Uttar Pradesh']
#     city = ['Lucknow', 'Kanpur', 'Agra']
#     data = {
#         "hospital_name": fake.hospital_name(),
#         "contact_number": fake.msisdn()[:10],
#         "email": fake.unique.email(),
#         "address": fake.address(),
#         "registration_number": fake.msisdn()[:8],
#         "owner_name": fake.owner_name(),
#         "owner_number": fake.msisdn()[:10],
#     }

def test_open_hospital_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click Master -> Hospital
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/button').click()
    time.sleep(1)

    #----Open hospital page
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[4]/div/div/div/div[7]/div[2]/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]').click()  #---Open the add hospital page
    time.sleep(2)

    # Assert that the hospital page is open
    assert "hospitals" in driver.current_url.lower()
    print("Hospital opened successfully")
