import dotenv
import os
from Model.Signup_Model import SignupRequest

class signuppagemother:
    def __init__(self):
        dotenv.load_dotenv()
        self.app_username = os.getenv("APP_USERNAME")
        self.app_password = os.getenv("APP_PASSWORD")

    def get(self) -> SignupRequest:
        return SignupRequest(
            username=self.app_username,
            password=self.app_password
        )
