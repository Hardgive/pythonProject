import pytest
from selenium import webdriver


def test_webdriver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def pytest_addoption(parser):
    url = parser.addoption("--url", action="store", default="https://www.saucedemo.com/")
    return url


def test_variables():
    dictionary = {
        'login_standard': 'standard_user',
        'login_locked': 'locked_out_user',
        'login_problem': 'problem_user',
        'login_performance': 'performance_glitch_user',
        'password': 'secret_sauce'
    }
    return dictionary


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")
