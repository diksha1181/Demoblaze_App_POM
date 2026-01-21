from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Laptop_Objects import LaptopObjects
import time


class LaptopFunctions(LaptopObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def open_laptops(self): 
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable(self.laptops)).click()
            time.sleep(2)  

        def open_laptop1(self):
            self.wait.until(EC.element_to_be_clickable(self.laptop1)).click()
            time.sleep(1)
           

        def cart(self):
            self.wait.until(EC.element_to_be_clickable(self.AddToCart)).click()
            time.sleep(1)
            
           
        def verify(self):
            self.wait.until(EC.alert_is_present())
            alert= self.driver.switch_to.alert
            print(alert.text)
            alert.accept()











