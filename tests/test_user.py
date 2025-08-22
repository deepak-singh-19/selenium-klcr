from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time

def generate_random_user_data():
    fake = Faker('en_In')
    user_type = ['Investigator', 'Report writer', 'Manager']
    role = ['Investigator', 'Report writer', 'Manager', 'Admin']
    state = ['Uttar Pradesh', 'Madhay Pradesh', 'Rajasthan', 'Bihar']
    city = ['Lucknow', 'Prayagraj', 'Agra', 'Indore', 'Bhopal', 'Jaipur', 'Udaipur', 'Patna']
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "user_type": random.choice(user_type),
        "role": random.choice(role),
        "email": fake.unique.email(),
        "mobile": fake.msisdn()[:10],
        "state": random.choice(state),
        "city": random.choice(city),
        "address": fake.address().replace("\n", " "),
        "aadhar_number": str(fake.random_int(min=100000000000, max=999999999999)),
        "pan_number": fake.bothify(text='?????####?'),  # Example format: ABCDE1234F
    }
    return data

def ensure_drawer_expanded(driver, wait):
    """
    Ensures the left-hand drawer/sidebar is expanded.
    Idempotent: does nothing if already expanded and 'System' is visible.
    """
    SYSTEM_XPATH = '//*[@id=":r4:"]'
    DRAWER_TOGGLE_XPATH = "/html/body/div/div[2]/div/div[1]/div/div[1]/button"
    # If the "System" link is not visible, the drawer is probably collapsed.
    if not driver.find_elements(By.XPATH, SYSTEM_XPATH):
        try:
            toggle = wait.until(EC.element_to_be_clickable((By.XPATH, DRAWER_TOGGLE_XPATH)))
            toggle.click()
            wait.until(EC.visibility_of_element_located((By.XPATH, SYSTEM_XPATH)))
        except Exception as e:
            print("Failed to auto-expand drawer:", str(e))
            # Optionally: assert False, "Drawer auto-expand failed"

def test_open_user_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    # driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    # time.sleep(2)

    #Click System -> User
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[2]/div[2]/span').click()
    time.sleep(2)

    #Open Add User page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button').click()
    time.sleep(2)

    #-----fill form with random data
    user_data = generate_random_user_data()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/div/div/input').send_keys(user_data['first_name'])
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[2]/div/div/input').send_keys(user_data['last_name'])
    time.sleep(2)

    #---Select the user type
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[3]/div/div[2]/div/div/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//li[normalize-space()='{user_data['user_type']}']").click()
    time.sleep(2)

    #--------Select the role data
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[4]/div/div[2]/div/div/input').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, f"//li[normalize-space()='{user_data['role']}']").click()
    # time.sleep(2)
    #
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[5]/div/div/input').send_keys(user_data['email'])
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[6]/div/div/div/input').send_keys(user_data['mobile'])
    # time.sleep(2)

    #------Select state data
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[7]/div/div/div/div/input').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, f"//li[normalize-space()='{user_data['state']}']").click()
    # time.sleep(2)

    #------Select city data
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[15]/div/div[2]/div/div/input').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, f"//li[normalize-space()='{user_data['city']}']").click()
    # time.sleep(2)
    #
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[9]/div/div/input').send_keys(user_data['address'])
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[17]/div/div/div/input').send_keys(user_data['aadhar_number'])
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/form/div/div[1]/div[18]/div/div/div/input').send_keys(user_data['pan_number'])
    # time.sleep(2)


    # driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button').click() #Click on the cancel icon
    # time.sleep(2)

    # Assert that the User page is open
    assert "user" in driver.current_url.lower()
    print("User page opened successfully")