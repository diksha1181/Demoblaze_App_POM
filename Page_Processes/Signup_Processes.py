from Page_Functions.Signup_Functions import SignupFunctions
from Data.Signup_Data import SignupData

class SignupProcess:

    def __init__(self, signup:SignupFunctions):
        self.signup = signup

    def run_process(self):
        data = SignupData()
        self.signup.open_signup()
        self.signup.enter_username(data.app_username)
        self.signup.enter_password(data.app_password)
        self.signup.click_signup()
        self.signup.verify_signup()