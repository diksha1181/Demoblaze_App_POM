from Page_Functions.Logout_Functions import LogoutFunctions


class LogoutProcess:

    def __init__(self, logout:LogoutFunctions):
        self.logout = logout

    def run_process(self):
        self.logout.click_logout()
        self.logout.verify_logout()
       