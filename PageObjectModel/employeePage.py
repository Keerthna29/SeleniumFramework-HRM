from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EmpPage:
    employeeLink=(By.XPATH,"//a/span[text()='PIM']")
    addEmployeeLink=(By.LINK_TEXT,"Add Employee")
    firstname=(By.NAME,"firstName")
    lastname=(By.NAME,"lastName")
    saveBtn=(By.CSS_SELECTOR,"button[type='submit']")

    def __init__(self,driver):
        self.driver=driver

    def click_empLink(self):
        return self.driver.find_element(*EmpPage.employeeLink)

    def click_addEmpLink(self):
        return self.driver.find_element(*EmpPage.addEmployeeLink)

    def get_firstname(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.presence_of_element_located((EmpPage.firstname)))

    def get_lastname(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((EmpPage.lastname)))


    def click_save(self):
        return self.driver.find_element(*EmpPage.saveBtn)