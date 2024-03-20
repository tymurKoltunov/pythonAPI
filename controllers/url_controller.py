import json

import requests
import os
from dotenv import load_dotenv

from utils.urls import URL

load_dotenv()


def get_jwt_token():
    url = os.environ.get("BASE_API_URL")
    token = os.environ.get("TOKEN")
    params = {"api_token": token}
    response = requests.post(url + URL.login.value, params=params)
    content = json.loads(response.content)
    return content['jwt']

def get_base_api_url():
    return os.environ.get("BASE_API_URL")
