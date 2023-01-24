import time
from time import sleep
from selenium.webdriver.common.by import By
import conftest
import selenium.webdriver.common
import allure
from allure_commons.types import AttachmentType


@allure.feature('Login')  # Группа функций теста
@allure.story('Логинимся на маркетплейс')  # Детально о выполняемой функции теста
@allure.severity('blocker')  # critical, normal, minor, trivial - Важность функции теста
def test_login(url):
    browser = conftest.setup_webdriver().get(url)
    login_button = browser.find_element(By.ID, "login-button")
    login_button_value = login_button.get_attribute("value")
    assert login_button_value == "Login"  # Проверяем, что кнопка Login существует
    browser.find_element(By.ID, "user-name").send_keys(conftest.test_variables().get("login_standard"))
    username_text = browser.find_element(By.ID, "user-name")
    assert username_text.get_attribute("value") == conftest.test_variables().get(
        "login_standard")  # Проверяем, что заполнили поле логина правильно
    browser.find_element(By.ID, "password").send_keys(conftest.test_variables().get("password"))
    password_text = browser.find_element(By.ID, "password")
    assert password_text.get_attribute("value") == conftest.test_variables().get(
        "password")  # Проверяем, что заполнили поле пароля правильно
    login_button.click()
    product_title = browser.find_element(By.CLASS_NAME, "title").get_property("innerText")
    assert product_title == "PRODUCTS"  # Проверяем авторизацию

@allure.feature("Cart")
@allure.story("Добавляем рюкзак в корзину кликнув кнопку ADD TO CART")
@allure.severity("critical")
def test_add_to_cart():
    browser = conftest.setup_webdriver()
    add_to_cart_button = browser.find_element((By.ID, "add-to-cart-sauce-labs-backpack"))
    assert add_to_cart_button.get_property("innerText") == "ADD TO CART" # Проверяем надпись на кнопке ADD TO CART
    add_to_cart_button.click()
    assert browser.find_element((By.CLASS_NAME, "shopping_cart_badge")).get_property("innerText") == "1" # Проверяем, что бейдж теперь над корзиной == 1

@allure.feature("Cart")
@allure.story("Убираем рюкзак из корзины кликнув кнопку REMOVE")
@allure.severity("critical")
def test_add_to_cart():
    browser = conftest.setup_webdriver()
    remove_backpack = browser.find_element((By.ID, "remove-sauce-labs-backpack"))
    assert remove_backpack.get_property("innerText") == "REMOVE" # Проверяем надпись на кнопке ADD TO CART
    remove_backpack.click()
    assert browser.find_element((By.CLASS_NAME, "shopping_cart_badge")).get_property("innerText") == None # Проверяем, что бейдж теперь над корзиной не присуствует

# Разделение на тесты - условное!