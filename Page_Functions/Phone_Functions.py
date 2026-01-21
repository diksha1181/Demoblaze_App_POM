from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Phone_Objects import PhoneObjects
import time


class PhoneFunctions(PhoneObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def open_home(self): 
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable(self.home)).click()
            time.sleep(2)  

        def open_phones(self):
            self.wait.until(EC.element_to_be_clickable(self.phones)).click()
            time.sleep(1)

        
        def open_phone1(self):
            self.wait.until(EC.element_to_be_clickable(self.phone1)).click()
            time.sleep(1)
           

        def cart(self):
            self.wait.until(EC.element_to_be_clickable(self.atc)).click()
            time.sleep(1)
            
           
        def verify(self):
            self.wait.until(EC.alert_is_present())
            alert= self.driver.switch_to.alert
            print(alert.text)
            alert.accept()











