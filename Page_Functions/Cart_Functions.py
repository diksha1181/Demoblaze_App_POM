from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Cart_Objects import CartObjects
import time
from Data.Cart_Data import fake

class CartFunctions(CartObjects):
   
        def __init__(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 15)

        def open_cart(self): 
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable(self.cart)).click()
            time.sleep(2)
            print("cart opened")

        def place_order(self):
            print("place order fxn")
            self.wait.until(EC.element_to_be_clickable(self.place_order_btn)).click()
            time.sleep(3)
            print("place order btn clicked.")

        def form_visibility(self):
             time.sleep(4)
             self.wait.until(EC.visibility_of_all_elements_located(self.form))
             time.sleep(2)

      
        def enter_name(self):
            self.driver.find_element(*self.name).send_keys(fake.name())

        def enter_country(self):
            self.driver.find_element(*self.country).send_keys(fake.country())

        def enter_city(self):
            self.driver.find_element(*self.city).send_keys(fake.city())

        def enter_card(self):
            self.driver.find_element(*self.card).send_keys(fake.credit_card_number())

        def enter_month(self):
            self.driver.find_element(*self.month).send_keys(fake.month())

        def enter_year(self):
            self.driver.find_element(*self.year).send_keys(fake.year())

        def click_purchase(self):
            self.driver.find_element(*self.purchase).click()
            time.sleep(1)
      
        def verify_successful_purchase(self):            
            self.wait.until(EC.element_to_be_clickable(self.ok)).click()
            time.sleep(2)         
            print("Returned to Home page . Order Placed Successfully ")
           
            










