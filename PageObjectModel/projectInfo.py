from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProjectInfo:

    timeMenu=(By.XPATH,"//a/span[text()='Time']")
    projectInfoLink=(By.XPATH,"//span[text()='Project Info ']")
    projectsLink=(By.LINK_TEXT,"Projects")
    addButton=(By.XPATH,"(//div/div/button[@type='button'])[3]")
    projectName=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    addCustomerButton=(By.XPATH,"(//button[@type='button'])[3]")
    customerName=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
    description=(By.XPATH,"(//div/textarea)[2]")
    saveButton=(By.XPATH,"//div[@class='oxd-form-actions orangehrm-form-action']/button[@type='submit']")
    saveProject=(By.XPATH,"//button[@type='submit']")

    def __init__(self,driver):
        self.driver=driver

    def click_timeMenu(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.presence_of_element_located((ProjectInfo.timeMenu)))


    def click_projectInfo(self):
        return self.driver.find_element(*ProjectInfo.projectInfoLink)

    def click_projects(self):
        return self.driver.find_element(*ProjectInfo.projectsLink)

    def click_addBtn(self):
        return self.driver.find_element(*ProjectInfo.addButton)

    def get_projectName(self):
        return self.driver.find_element(*ProjectInfo.projectName)

    def click_addCustomer(self):
        return self.driver.find_element(*ProjectInfo.addCustomerButton)

    def get_customerName(self):
        return self.driver.find_element(*ProjectInfo.customerName)

    def get_description(self):
        return self.driver.find_element(*ProjectInfo.description)

    def click_saveBtn(self):
        return self.driver.find_element(*ProjectInfo.saveButton)

    def save_Project(self):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(expected_conditions.presence_of_element_located((ProjectInfo.saveProject)))
