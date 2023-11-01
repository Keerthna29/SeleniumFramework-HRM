import time

import pytest

from PageObjectModel.dashboardPage import DashboardPage
from PageObjectModel.loginPage import LoginPage
from PageObjectModel.employeePage import EmpPage
from PageObjectModel.projectInfo import ProjectInfo
from testData.addEmployeeData import AddEmployeeData
from testData.addProjectData import AddProjectData
from testData.userloginData import UserLoginData
from utilities.baseclass import BaseClass


class TestHRM(BaseClass):

    def test_login(self,getData_UserLogin):
        global log
        log = self.get_logger()
        log.info("User Login")

        loginPage=LoginPage(self.driver)
        loginPage.get_username().send_keys(getData_UserLogin["username"])
        loginPage.get_password().send_keys(getData_UserLogin["password"])
        loginPage.click_loginBtn().click()

        log.info(self.driver.title)


    def test_addEmployee(self,getData_EmployeeDetails):
        log.info("Adding Employee Details")

        employeePage=EmpPage(self.driver)
        employeePage.click_empLink().click()
        employeePage.click_addEmpLink().click()
        time.sleep(4)
        employeePage.get_firstname().send_keys(getData_EmployeeDetails["firstname"])
        employeePage.get_lastname().send_keys(getData_EmployeeDetails["lastname"])
        employeePage.click_save().click()
        time.sleep(4)

    def test_addProject(self,getData_ProjectDetails):
        log.info("Adding Project Details")

        projectpage=ProjectInfo(self.driver)
        projectpage.click_timeMenu().click()
        projectpage.click_projectInfo().click()
        projectpage.click_projects().click()
        projectpage.click_addBtn().click()
        projectpage.get_projectName().send_keys(getData_ProjectDetails["projectname"])
        projectpage.click_addCustomer().click()
        projectpage.get_customerName().send_keys(getData_ProjectDetails["customername"])
        projectpage.get_description().send_keys(getData_ProjectDetails["description"])
        projectpage.click_saveBtn().click()
        time.sleep(5)
        projectpage.save_Project().click()
        time.sleep(5)

    def test_verifyDashboard(self):
        dashboardPage=DashboardPage(self.driver)
        dashboardPage.click_dashboardMenu().click()
        time.sleep(5)
        # javascript executor
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        verify_copyrights=dashboardPage.verify_copy_rights_year().text
        assert "© 2005 - 2023 " in verify_copyrights
        log.info(verify_copyrights)
        self.driver.get_screenshot_as_file("Dashboard.png")
        # logout
        dashboardPage.click_userMenu().click()
        dashboardPage.click_userLogout().click()
        time.sleep(5)

    @pytest.fixture(params=UserLoginData.test_data_userLogin)
    def getData_UserLogin(self,request):
        return request.param

    @pytest.fixture(params=AddEmployeeData.test_data_addEmp)
    def getData_EmployeeDetails(self,request):
        return request.param

    @pytest.fixture(params=AddProjectData.test_data_projectDetails)
    def getData_ProjectDetails(self,request):
        return request.param






        # alert=self.driver.switch_to.alert
        # alert.accept()


