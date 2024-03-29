from enum import Enum


class URL(Enum):
    login = "/login"
    projects = "/projects"
    project_id = "/api_tests"
    suites = "/suites"
    tests = "/tests"
