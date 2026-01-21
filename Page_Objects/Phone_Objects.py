from selenium.webdriver.common.by import By

class PhoneObjects:     
    home= (By.CSS_SELECTOR,"nav[class='navbar navbar-toggleable-md bg-inverse'] li:nth-child(1)")  
    phones = (By.LINK_TEXT, "Phones")
    phone1= (By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")
    phone2= (By.XPATH, "//a[normalize-space()='Nokia lumia 1520']")
    phone3= (By.XPATH, "//a[normalize-space()='Nexus 6']")
    phone4= (By.XPATH, "//a[normalize-space()='Samsung galaxy s7']")
    phone5= (By.XPATH, "//a[normalize-space()='Iphone 6 32gb']")
    atc = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")


    
    









