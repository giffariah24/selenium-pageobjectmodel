from selenium.webdriver.common.by import By

# Page Elements
class RegisterPage:
    # Locators
    txtbox_email = "email"
    txtbox_password = "reg_password"
    txtbox_register = "register"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    def setEmail(self, email):
        emailtxt = self.driver.find_element(By.NAME, self.txtbox_email)
        emailtxt.send_keys(email)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password)
        passwordtxt.send_keys(password)

    def clickRegister(self):
        self.driver.find_element(By.NAME, self.txtbox_register).click()