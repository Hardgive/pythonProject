import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def url(request):
    return request.config.getoption("--url")


def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = Options()
        if headless == 'true':
            options.add_argument('--headless')
        elif headless == 'false':
            options.add_argument('')
        else:
            print(f'Неверное значение параметра --headless={headless}. Передано как значение по умолчанию --headless=true')
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


def headless(request):
    return request.config.getoption("--headless")


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://www.saucedemo.com/")
    parser.addoption("--headless", action="store", default="12315")


def test_variables():
    dictionary = {
        'login_standard': 'standard_user',
        'login_locked': 'locked_out_user',
        'login_problem': 'problem_user',
        'login_performance': 'performance_glitch_user',
        'password': 'secret_sauce'
    }
    return dictionary
