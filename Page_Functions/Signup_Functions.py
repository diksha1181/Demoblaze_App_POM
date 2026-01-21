from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Signup_Objects import SignupObjects
import time


class SignupFunctions(SignupObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def open_signup(self): 
            self.wait.until(EC.element_to_be_clickable(self.signup)).click()
            time.sleep(2)  

        def enter_username(self,username):
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located(self.username))
            self.driver.find_element(*self.username).send_keys(username)

        def enter_password(self,password):
            self.driver.find_element(*self.password).send_keys(password)
                

        def click_signup(self):
            self.driver.find_element(*self.signup_Button).click()
            time.sleep(1)

        def verify_signup(self):
            self.wait.until(EC.alert_is_present())
            alert= self.driver.switch_to.alert
            print("Alert Text :", alert.text)
            alert.accept()
            self.wait.until(EC.element_to_be_clickable(self.close_Button)).click()

            

            
            










