import pytest
from selenium.webdriver.common.by import By
import conftest
import allure
import selenium.webdriver.support.expected_conditions as EC

import selenium.webdriver.common
import selenium.common.exceptions as exceptions
from time import sleep


@pytest.mark.usefixtures("driver_init", "url")
class TestSaucedemo:
    @allure.feature('Login')  # Группа функций теста
    @allure.story('Логинимся на маркетплейс')  # Детально о выполняемом методе теста
    @allure.severity('blocker')  # critical, normal, minor, trivial - Важность функции теста
    def test_login(self, url):
        browser = self.driver
        browser.get(url)
        login_button = browser.find_element(By.ID, "login-button")
        login_button_value = login_button.get_attribute("value")
        assert login_button_value == "Login"  # Проверяем, что кнопка Login существует
        browser.find_element(By.ID, "user-name").send_keys(conftest.test_variables().get("login_standard"))
        username_text = browser.find_element(By.ID, "user-name")
        with allure.step("Проверяем, что заполнили поле логина правильно"):
            assert username_text.get_attribute("value") == conftest.test_variables().get("login_standard")
        browser.find_element(By.ID, "password").send_keys(conftest.test_variables().get("password"))
        password_text = browser.find_element(By.ID, "password")
        with allure.step("Проверяем, что заполнили поле пароля правильно"):
            assert password_text.get_attribute("value") == conftest.test_variables().get("password")  # Проверяем, что заполнили поле пароля правильно
        login_button.click()
        product_title = browser.find_element(By.CLASS_NAME, "title").get_property("innerText")
        assert product_title == "Products"  # Проверяем авторизацию

    @pytest.mark.cart
    @allure.feature("Cart")
    @allure.story("Добавляем рюкзак в корзину кликнув кнопку ADD TO CART")
    @allure.severity("critical")
    def test_add_to_cart(self):
        browser = self.driver
        add_to_cart_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        assert add_to_cart_button.get_property("innerText") == "Add to cart"  # Проверяем надпись на кнопке ADD TO CART
        add_to_cart_button.click()
        assert browser.find_element(By.CLASS_NAME, "shopping_cart_badge").get_property("innerText") == "1"  # Проверяем, что бейдж теперь над корзиной == 1

    @pytest.mark.cart
    @allure.feature("Cart")
    @allure.story("Убираем рюкзак из корзины кликнув кнопку REMOVE")
    @allure.severity("critical")
    def test_remove_from_cart(self):
        browser = self.driver
        remove_backpack = browser.find_element(By.ID, "remove-sauce-labs-backpack")
        assert remove_backpack.get_property("innerText") == "Remove"  # Проверяем надпись на кнопке ADD TO CART
        assert EC.element_to_be_clickable(remove_backpack)  # Проверяем его кликабельность
        remove_backpack.click()
        badge = browser.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badge) == 0  # Проверяем, что бейджа теперь нет



# pytest --url=https://www.saucedemo.com/ - запуск всех тестов
# pytest -m "not cart" --url=https://www.saucedemo.com/ - запуск всех тестов, кроме маркера cart

# Чтобы посмотреть отчет allure нужно запустить Powershell, перейти в дирректорию проекта и запустить команду allure serve report и тогда откроется html страница с отчетом