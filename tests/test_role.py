# tests/test_role.py
from pages.signin_page import signinPage
from selenium.webdriver.common.by import By
import time

def test_open_role_page(driver):
    signinPage(driver).login("info@klcrinvestigations.com", "Insurance@123")


    #Click on left drawer button
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # Click System -> Role
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[3]/div/div/div/div[1]/div[2]/span').click()
    time.sleep(2)

    # Open the Add role page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/button[2]').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'roleName').send_keys("Admin") # enter the role name
    time.sleep(2)

    #close the add role page
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/form/div[3]/button[2]').click()
    time.sleep(2)

    # open view role page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[5]/div/button[1]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button').click() # close the view role page

    # open edit role page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[5]/div/button[2]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/button').click() # close the edit role page
    time.sleep(2)

    #open the delete role confirmation message
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[5]/div/button[3]').click()  #Open the delete confirmation message
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/button[2]').click()  #click on the not now button
    time.sleep(2)

    # Assert that the Role page is open
    assert "role" in driver.current_url.lower()
    print("Role page opened successfully")
