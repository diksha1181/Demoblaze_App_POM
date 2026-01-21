from selenium.webdriver.common.by import By

class SignupObjects:       
    signup = (By.ID,"signin2")
    username= (By.ID ,"sign-username")
    password = (By.ID, "sign-password")
    signup_Button = (By.CSS_SELECTOR, "button[onclick='register()']")
    close_Button = (By.CSS_SELECTOR,"div[id='signInModal'] div[class='modal-footer'] button:nth-child(1)")
 










