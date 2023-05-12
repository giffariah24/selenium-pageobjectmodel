from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LoginPageObjects import LoginPage

import time

class TestLogin:
    def test_login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://demostore.supersqa.com/my-account/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail("vinej88687@momoshe.com")
        time.sleep(1)

        self.lp.setPassword("Mukidi123")
        time.sleep(1)

        self.lp.clickLogin()
        time.sleep(1)

        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]/a'),
                'Log out'
            )
        )
