import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import AuthPageLocators
from locators import MainPageLocators
from locators import RegistPageLocators

class TestUserRegistration:

    def test_regist_user(self, open_main_page):
        fake = Faker()
        driver = open_main_page

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.REGIST_BUTTON)
        ).click()

        email = fake.email()
        password = "test123!"

        driver.find_element(*RegistPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistPageLocators.REGIST_BUTTON).click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOGO_BUTTON)
        )
        assert element.is_displayed(), "Элемент 'circleSmall' не отображается"

        user_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        assert user_element.is_displayed(), "Элемент с текстом 'User.' найден, но не отображается"

    @pytest.mark.parametrize("invalid_email", [
        "userexample.com",  # Нет символа @
        "user@example",     # Неверный домен
        "user@.com",        # Неверный домен
        "user@example.c",   # Слишком короткое расширение
        "user@example..com",# Двойная точка
        "user@exampl#e.com",# Недопустимые символы
    ])
    def test_registration_with_invalid_email(self, open_main_page, invalid_email):
        driver = open_main_page

        # 1. Нажать кнопку "Вход и регистрация"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # 2. Нажать кнопку "Нет аккаунта"
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.REGIST_BUTTON)
        )
        register_link.click()

        # 3. Заполнить поля формы регистрации
        driver.find_element(*RegistPageLocators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*RegistPageLocators.PASSWORD_INPUT).send_keys("ValidPass123!")
        driver.find_element(*RegistPageLocators.SUBMIT_PASSWORD_INPUT).send_keys("ValidPass123!")

        # 4. Нажать кнопку "Создать аккаунт"
        driver.find_element(*RegistPageLocators.REGIST_BUTTON).click()

        # 5. Проверить, что поля выделены красным
        error_containers = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(RegistPageLocators.RED_ERROR)
        )
        assert len(error_containers) == 3, "Выделено красным что-то лишнее"

        for container in error_containers[:3]:  # берем только первые 3, если есть лишние
            assert container.is_displayed(), "Контейнер не отображается"
            assert "input_inputError__fLUP9" in container.get_attribute("class"), "Класс ошибки не найден"

        # 6. Проверить сообщение "Ошибка" под полем Email
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistPageLocators.MESSAGE_ERROR)
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == "Ошибка"

        # 7. Проверить, что переход на главную страницу не произошел
        assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/regiatration", "Произошел нежелательный переход на главную страницу"

    def test_registration_with_existing_user(self, open_main_page):
        driver = open_main_page

        # 1. Нажать кнопку "Вход и регистрация"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # 2. Нажать кнопку "Нет аккаунта"
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.REGIST_BUTTON)
        )
        register_link.click()

        # 3. Заполнить поля формы регистрации данными существующего пользователя
        existing_email = "test@gmail.com" 
        existing_password = "test123!"        

        driver.find_element(*RegistPageLocators.EMAIL_INPUT).send_keys(existing_email)
        driver.find_element(*RegistPageLocators.PASSWORD_INPUT).send_keys(existing_password)
        driver.find_element(*RegistPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(existing_password)

        # 4. Нажать кнопку "Создать аккаунт"
        driver.find_element(*RegistPageLocators.REGIST_BUTTON).click()

        # 5. Проверить, что поля выделены красным
        error_containers = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(RegistPageLocators.RED_ERROR)
        )
        assert len(error_containers) == 3, "Выделено красным что-то лишнее"

        for container in error_containers[:3]:
            assert container.is_displayed(), "Контейнер не отображается"
            assert "input_inputError__fLUP9" in container.get_attribute("class"), "Класс ошибки не найден"

        # 6. Проверить сообщение "Ошибка" под полем Email
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistPageLocators.MESSAGE_ERROR)
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == "Ошибка"

        # 7. Проверить, что переход на главную страницу не произошел
        assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/regiatration", "Произошел нежелательный переход на главную страницу"

