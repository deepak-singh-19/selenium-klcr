from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

def test_open_role_page(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Login
    signinPage(driver).login("info@klcrinvestigations.com", "Insurance@123")

    # 2. Ensure the drawer is always expanded, regardless of device
    ensure_drawer_expanded(driver, wait)

    # 3. Navigate: System -> Role
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='System']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[1]/div[2]/span'))).click()
    time.sleep(2)

    # 4. Open 'Add Role' modal
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]'))).click()
    time.sleep(2)

    # 5. Fill form: Role name = Admin
    wait.until(EC.visibility_of_element_located((By.NAME, 'roleName'))).send_keys("Admin")
    time.sleep(2)

    # 6. Close 'Add Role' modal (cancel button)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()
    time.sleep(2)

    # 7. View Role
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[1]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()
    time.sleep(2)

    # 8. Edit Role
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[2]'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button'))).click()
    time.sleep(2)

    # 9. Delete Role (but cancel deletion)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div/button[3]'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/button[2]'))).click()
    time.sleep(2)

    # #10. Show Entries
    # wait.until(EC.element_to_be_clickable((By.ID, 'demo-simple-select'))).click()
    # time.sleep(2)

    #11. Filter
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/button'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/div/form/div/div[1]/div/label[1]/span[1]'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/div/form/div/div[2]/button[1]'))).click()
    time.sleep(2)

    #12. Clear filter
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/button'))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r3t:"]'))).click()
    time.sleep(2)

    #13. Search functionality
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/input'))).send_keys('Backend')
    time.sleep(5)
    #clear the search field
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/div'))).click() # This clears the input field programmatically
    time.sleep(5)

    # Final assertion
    assert "role" in driver.current_url.lower()
    print("Role page opened successfully")

    # input("\nPress ENTER to close the browser...")
    # driver.quit()
