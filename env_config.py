import os
from dotenv import load_dotenv


class EnvConfig:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL')
