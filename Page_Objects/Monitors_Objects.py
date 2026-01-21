from selenium.webdriver.common.by import By

class MonitorObjects:     
    home= (By.CSS_SELECTOR,"nav[class='navbar navbar-toggleable-md bg-inverse'] li:nth-child(1)")  
    monitors = (By.LINK_TEXT, "Monitors")
    monitor1= (By.XPATH, "//a[normalize-space()='Apple monitor 24']")
    atc = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    









