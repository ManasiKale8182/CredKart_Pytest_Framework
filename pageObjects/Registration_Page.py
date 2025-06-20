'''
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    self.text_name_id = "name"
    text_confirm_password_id = "password-confirm"


    def Enter_Name(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, self.text_name_id)))
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def Enter_Confirm_Password(self, confirm_password):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(confirm_password)
        '''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.text_name_id = "name"  # ✅ Add missing locator
        self.text_confirm_password_id = "password-confirm"  # ✅ Add confirm password locator

    def Enter_Name(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, self.text_name_id)))
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def Enter_Confirm_Password(self, confirm_password):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(confirm_password)
