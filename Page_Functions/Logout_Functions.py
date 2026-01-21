from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Logout_Objects import LogoutObjects
import time


class LogoutFunctions(LogoutObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def click_logout(self): 
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable(self.logout)).click()
            time.sleep(2)  

        def verify_logout(self):           
         self.wait.until(EC.visibility_of_element_located(self.first))
         print("Log out Successful")
            










