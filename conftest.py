import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators
from locators import MainPageLocators

email= 'tester231@gmail.com'
password = 'test123!'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/ ")
    return driver

# Фикстура для авторизации
@pytest.fixture
def login(open_main_page):
    driver = open_main_page

    # 1. Нажать кнопку "Вход и регистрация"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # 2. Заполнить поля формы авторизации
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)
    )
    email_field.send_keys(email)

    password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPageLocators.PASSWORD_INPUT)
        )
    password_field.send_keys(password)

    # 3. Нажать кнопку "Войти"
    submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)
        )
    submit_button.click()
    return driver