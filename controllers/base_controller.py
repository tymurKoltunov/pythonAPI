import json

import requests
import os
from dotenv import load_dotenv

from utils.urls import URL

load_dotenv()


class BaseController:
    PROJECT_ID = "/api_tests"
    LOGIN = "/login"
    PROJECTS = "/projects"
    SUITES = "/suites"
    TESTS = "/tests"
    TOKEN = None

    def withJwtToken(self, token):
        self.TOKEN = token
        return self

    def get_base_api_url(self):
        return os.environ.get("BASE_API_URL")
