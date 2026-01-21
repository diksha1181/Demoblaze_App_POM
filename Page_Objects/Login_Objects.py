from selenium.webdriver.common.by import By

class LoginObjects:       
    login = (By.ID, "login2")
    username=(By.ID, "loginusername")
    password = (By.ID, "loginpassword")
    Login_Button = (By.CSS_SELECTOR,"#logInModal .btn.btn-primary")
    Close_Button = (By.CSS_SELECTOR,"div[id='logInModal'] div[class='modal-footer'] button:nth-child(1)")
    welcome_text = (By.ID,"nameofuser")










