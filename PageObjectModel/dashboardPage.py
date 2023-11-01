from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage:

    dashboardmenu=(By.XPATH,"//a/span[text()='Dashboard']")
    verifyCopyrights=(By.XPATH,"//div[@class='oxd-layout-footer']")
    usernameMenu=(By.XPATH,"//p[@class='oxd-userdropdown-name']")
    logout=(By.LINK_TEXT,"Logout")

    def __init__(self,driver):
        self.driver=driver

    def click_dashboardMenu(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.presence_of_element_located((DashboardPage.dashboardmenu)))


    def verify_copy_rights_year(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((DashboardPage.verifyCopyrights)))

    def click_userMenu(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((DashboardPage.usernameMenu)))


    def click_userLogout(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((DashboardPage.logout)))




