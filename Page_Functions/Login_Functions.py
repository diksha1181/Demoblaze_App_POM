from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Login_Objects import LoginObjects
import time


class LoginFunctions(LoginObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def open_login(self): 
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable(self.login)).click()
            time.sleep(2)  

        def enter_username(self,username):
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located(self.username))
            self.driver.find_element(*self.username).send_keys(username)

        def enter_password(self,password):
            self.driver.find_element(*self.password).send_keys(password)
                

        def click_login(self):
            self.driver.find_element(*self.Login_Button).click()
            time.sleep(1)

        def verify_login(self):
            welcome_text = self.wait.until(EC.visibility_of_element_located(self.welcome_text))
            if(welcome_text):
                print("Login successful! - ",welcome_text.text)
            










