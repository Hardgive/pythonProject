import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def url(request):
    return request.config.getoption("--url")


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=options)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


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
