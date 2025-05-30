import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from locators import MainPageLocators
from locators import AuthPageLocators
from locators import AdPageLocators
from locators import UserPageLocators

class Test_Add_Commits:
    def test_ad_commits_with_unauthorized(self, open_main_page):
        driver = open_main_page

        # 1. Нажать кнопку "Разместить объявление"
        create_ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.NEW_AD_BUTTON)
        )
        create_ad_button.click()

        # 2. Проверить появление модального окна
        modal_window = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPageLocators.WINDOW_AUTH)  
        )
        assert modal_window.is_displayed(), "Модальное окно не отображается"

        # 3. Проверить заголовок модального окна
        modal_title = driver.find_element(*AuthPageLocators.TOP_TEXT)
        assert modal_title.is_displayed(), "Заголовок модального окна не отображается"

    def test_add_commits_with_authenticated(self, login):
        driver = login 

        # 1. Перейти на страницу создания объявления
        max_retries = 3
        for attempt in range(max_retries):
            try:
                create_ad_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(MainPageLocators.NEW_AD_BUTTON)
                )
                create_ad_button.click()
                print("Кнопка успешно нажата")
                break
            except StaleElementReferenceException:
                print(f"Элемент стал stale, попытка {attempt + 1} из {max_retries}")
                if attempt == max_retries - 1:
                    raise Exception("Не удалось кликнуть по кнопке после нескольких попыток")

        # 2. Заполнить поле "Название"
        title_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdPageLocators.NAME_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", title_field)
        title_field.send_keys("Тестовое объявление")

        # 3. Заполнить поле "Описание товара"
        description_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.DISC_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", description_field)
        description_field.send_keys("Это тестовое описание товара для автоматизированного тестирования.")

        # 4. Заполнить поле "Стоимость" (только числа)
        price_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.PRICE_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", price_field)
        price_field.send_keys("5000")

        # 5. Выбрать категорию из кастомного dropdown
        category_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CATEGORY)
        )
        category_dropdown.click()

        category_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CATEGORY_BOOK)
        )
        category_option.click()

        # 6. Выбрать город из кастомного dropdown
        city_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CITY)
        )
        city_dropdown.click()

        city_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CITY_MOSCOW)
        )
        city_option.click()

        # 7. Выбрать состояние товара (RadioButton)
        condition_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdPageLocators.RADIOBUTTON_NEW)
        )
        condition_label.click()

        # 8. Нажать кнопку "Опубликовать"
        publish_button = driver.find_element(*AdPageLocators.SUBMIT_AD_BUTTON)
        publish_button.click()

        # 9. Перейти в профиль пользователя
        # Найти кнопку с повторными попыткам  
        for attempt in range(max_retries):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(MainPageLocators.LOGO_BUTTON)
                )
                element.click()
                print("Кнопка успешно нажата")
                break
            except StaleElementReferenceException:
                print(f"Элемент стал stale, попытка {attempt + 1} из {max_retries}")
                if attempt == max_retries - 1:
                    raise Exception("Не удалось кликнуть по кнопке после нескольких попыток")

        # 10. Проверить, что объявление отображается в блоке "Мои объявления"
        first_card = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(UserPageLocators.USER_FIRST_AD)
        )
        # Проверить заголовок
        title_element = WebDriverWait(first_card, 10).until(
            EC.visibility_of_element_located(UserPageLocators.TOP_TEXT_ON_AD)
        )
        assert title_element.text == "Тестовое объявление", f"Ожидалось 'Тестовое объявление', получено '{title_element.text}'"

        # Проверить город
        city = first_card.find_element(*UserPageLocators.CITY_ON_AD).text
        assert city == "Москва", f"Ожидалось 'Москва', получено '{city}'"

        # Проверить цену
        price = first_card.find_element(*UserPageLocators.PRICE_ON_AD).text
        assert price == "5 000 ₽", f"Ожидалось '5 000 ₽', получено '{price}'"