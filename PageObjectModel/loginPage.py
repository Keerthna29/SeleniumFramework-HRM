from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    username=(By.NAME,"username")
    password=(By.NAME,"password")
    loginBtn=(By.XPATH,"//button[@type='submit']")

    def __init__(self,driver):
        self.driver=driver

    def get_username(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.presence_of_element_located((LoginPage.username)))

    def get_password(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((LoginPage.password)))


    def click_loginBtn(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((LoginPage.loginBtn)))
