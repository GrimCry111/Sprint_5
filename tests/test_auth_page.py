import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestUserAuth:
    # Тест: успешный вход пользователя
    def test_successful_login(self, login):
        driver = login

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOGO_BUTTON)
        )
        assert element.is_displayed(), "Элемент 'circleSmall' не отображается"

        user_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        assert user_element.is_displayed(), "Элемент с текстом 'User.' найден, но не отображается"

    def test_successful_logout(self,login):
        driver = login

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)
        ).click()

        element = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.LOGO_BUTTON)
        )
        assert element, "Элемент 'circleSmall' не отображается"

        user_element = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.USER_NAME)
        )
        assert user_element, "Элемент с текстом 'User.' найден, но не отображается"

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается"
