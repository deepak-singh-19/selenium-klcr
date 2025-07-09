from pages.signin_page import signinPage
import time
from selenium.webdriver.common.by import By

def test_open_reports_page(driver):
    # ── 1. Sign in ─────────────────────────────────────────────
    signin = signinPage(driver)
    signin.login("info@klcrinvestigations.com", "Insurance@123")

    # ── 2. Open the left‑hand drawer (hamburger) ───────────────
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(2)

    # setting > Reports
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[8]/button').click()
    # time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[2]/ul/div[9]/div[2]/span').click()
    time.sleep(2)

    #Reports > open Case summary report
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]').click()
    print('The case summary report is opened')
    time.sleep(4)

    #Reports > open case status reports page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]').click()
    print('The case status report is opened')
    time.sleep(4)

    #Reports > open investigator assignment report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[4]').click()
    print('The investigator assignment report is opened')
    time.sleep(4)

    #Reports > open investigation service report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[5]').click()
    print('The investigation service report is opened')
    time.sleep(4)

    #Reports > open pre qc review report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[6]').click()
    print('The Pre QC Review report is opened')
    time.sleep(4)

    #Reports > open investigation completion timeline report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[7]').click()
    print('The investigation completion timeline report is opened')
    time.sleep(4)

    #Reports > open case closure report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[8]').click()
    print('The case closure report is opened')
    time.sleep(4)

    #Reports > open report submission report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[9]').click()
    print('The report submission report is opened')
    time.sleep(4)

    #Reports > open user activity log report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[10]').click()
    print('The user activity log report is opened')
    time.sleep(4)

    #Reports > open manager performance report page
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[11]').click()
    print('The manager performance report is opened')
    time.sleep(4)

    # Assert that the Reports page is open
    assert "case-report" in driver.current_url.lower()
    print("Case Report opened successfully")
