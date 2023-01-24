from time import sleep
from selenium.webdriver.common.by import By
from conftest import test_variables
import conftest
import selenium.webdriver.common


try:
    def test_login(url):
        browser = conftest.test_webdriver(url)
        login_button = browser.find_element(By.ID, "login-button")
        login_button_value = login_button.get_attribute("value")
        assert login_button_value == "Login" # Проверяем, что кнопка Login существует
        browser.find_element(By.ID, "user-name").send_keys(test_variables().get('login_standard'))
        browser.find_element(By.ID, "password").send_keys(test_variables().get('password'))
        login_button.click()
        sleep(5) # Для отладки
        product_title = browser.find_element(By.CLASS_NAME, "title").get_property("innerText")
        assert product_title == "PRODUCTS" # Проверяем авторизацию
        return browser
except selenium.common.exceptions:
    raise Exception("[E][id=001] Тут могла быть Ваша реклама!")

