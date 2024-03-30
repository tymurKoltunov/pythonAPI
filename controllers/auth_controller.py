import json
import os

import requests
from dotenv import load_dotenv

from controllers.base_controller import BaseController

load_dotenv()


class AuthController(BaseController):
    def get_jwt_token(self):
        url = os.environ.get("BASE_API_URL")
        token = os.environ.get("TOKEN")
        params = {"api_token": token}
        response = requests.post(url + self.LOGIN, params=params)
        content = json.loads(response.content)
        return content['jwt']
