import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def url(request):
    return request.config.getoption("--url")


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://www.saucedemo.com/")


def test_variables():
    dictionary = {
        'login_standard': 'standard_user',
        'login_locked': 'locked_out_user',
        'login_problem': 'problem_user',
        'login_performance': 'performance_glitch_user',
        'password': 'secret_sauce'
    }
    return dictionary
