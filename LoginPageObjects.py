from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    txtbox_email = "username"
    txtbox_password = "password"
    txtbox_login = "login"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    def setEmail(self, email):
        emailtxt = self.driver.find_element(By.NAME, self.txtbox_email)
        emailtxt.send_keys(email)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.NAME, self.txtbox_password)
        passwordtxt.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME, self.txtbox_login).click()
