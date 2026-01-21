import dotenv
import os

class ConfigData:
    def __init__(self):
        dotenv.load_dotenv()
        self.BASE_URL = os.getenv("BASE_URL")