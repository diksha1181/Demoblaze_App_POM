import dotenv
import os
from Model.Login_Model import LoginRequest

class loginpagemother:
    def __init__(self):
        dotenv.load_dotenv()
        self.app_username = os.getenv("APP_USERNAME")
        self.app_password = os.getenv("APP_PASSWORD")

    def get(self) -> LoginRequest:
        return LoginRequest(
            username=self.app_username,
            password=self.app_password
        )
