from selenium import webdriver
from RegisterPageObjects import RegisterPage
import time

# Test Methods

class TestRegister:
    def test_register(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = options)
        self.driver.get("http://demostore.supersqa.com/my-account/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        self.rp = RegisterPage(self.driver)

        self.rp.setEmail("vinej88687@momoshe.com")
        time.sleep(2)

        self.rp.setPassword("Secret123!")
        time.sleep(2)

        self.rp.clickRegister()

        self.act_url = self.driver.current_url
        assert self.act_url == "http://demostore.supersqa.com/my-account/"