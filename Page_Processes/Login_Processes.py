from Page_Functions.Login_Functions import LoginFunctions
from Data.Login_Data import LoginData

class LoginProcess:

    def __init__(self, login:LoginFunctions):
        self.login = login

    def run_process(self):
        data = LoginData()
        self.login.open_login()
        self.login.enter_username(data.app_username)
        self.login.enter_password(data.app_password)
        self.login.click_login()
        self.login.verify_login()