import dotenv
import os

class LoginData:
    def __init__(self):
        dotenv.load_dotenv()
        self.app_username = os.getenv("APP_USERNAME")
        self.app_password = os.getenv("APP_PASSWORD")