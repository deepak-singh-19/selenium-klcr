from selenium.webdriver.common.by import By

class signinPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://staging.klcrinvestigations.com/auth/signin/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        #self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/div[1]/div/input').send_keys(username)
        self.driver.find_element(By.NAME, 'email').send_keys(username)
        #self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/form/button').click()
        #self.driver.find_element(By.ID, ":r1er:").click()
