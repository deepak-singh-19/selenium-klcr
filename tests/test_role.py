from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ensure_drawer_expanded(driver, wait):
    """
    Ensures the left-hand drawer/sidebar is expanded.
    Idempotent: does nothing if already expanded and 'System' is visible.
    """
    SYSTEM_XPATH = '//*[@id=":r39:"]'
    DRAWER_TOGGLE_XPATH = '//*[@id=":r0:"]'
    # If the "System" link is not visible, the drawer is probably collapsed.
    if not driver.find_elements(By.XPATH, SYSTEM_XPATH):
        try:
            toggle = wait.until(EC.element_to_be_clickable((By.XPATH, DRAWER_TOGGLE_XPATH)))
            toggle.click()
            wait.until(EC.visibility_of_element_located((By.XPATH, SYSTEM_XPATH)))
        except Exception as e:
            print("Failed to auto-expand drawer:", str(e))
            # Optionally: assert False, "Drawer auto-expand failed"

def test_open_role_page(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Login
    signinPage(driver).login("info@klcrinvestigations.com", "Insurance@123")

    # 2. Ensure the drawer is always expanded, regardless of device
    ensure_drawer_expanded(driver, wait)

    # 3. Navigate: System -> Role
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='System']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[1]/div[2]/span'))).click()

    # 4. Open 'Add Role' modal
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]'))).click()

    # 5. Fill form: Role name = Admin
    wait.until(EC.visibility_of_element_located((By.NAME, 'roleName'))).send_keys("Admin")

    # 6. Close 'Add Role' modal (cancel button)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()

    # 7. View Role
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[1]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()

    # 8. Edit Role
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[2]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()

    # 9. Delete Role (but cancel deletion)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[3]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/button[2]'))).click()

    # 10. Final assertion
    assert "role" in driver.current_url.lower()
    print("Role page opened successfully")
