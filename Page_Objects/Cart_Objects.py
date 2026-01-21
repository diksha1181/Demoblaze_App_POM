from selenium.webdriver.common.by import By

class CartObjects:       
    cart = (By.LINK_TEXT, "Cart")
    place_order_btn = (By.CSS_SELECTOR, ".btn.btn-success")
    form = (By.CSS_SELECTOR,"#orderModal")
    name = (By.ID,"name")
    country = (By.ID,"country")
    city = (By.ID,"city")
    card = (By.ID,"card")
    month = (By.ID,"month")
    year = (By.ID,"year")
    purchase = (By.XPATH,"//button[normalize-space()='Purchase']")
    ok = (By.CSS_SELECTOR,".confirm.btn.btn-lg.btn-primary")

    









