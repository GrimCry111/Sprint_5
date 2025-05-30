from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    LOGO_BUTTON = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name' and text()='User.']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    NEW_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")

class AuthPageLocators:
    WINDOW_AUTH = (By.CLASS_NAME, "popUp_shell__LuyqR")
    TOP_TEXT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGIST_BUTTON = (By.XPATH, "//button[.//text()='Нет аккаунта']")

class RegistPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    REGIST_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    RED_ERROR = (By.CLASS_NAME, "input_inputError__fLUP9")
    MESSAGE_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")

class AdPageLocators:
    NAME_AD = (By.NAME, "name")
    DISC_AD = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_AD = (By.NAME, "price")
    DROPDOWN_CATEGORY = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]")
    DROPDOWN_CATEGORY_BOOK = (By.XPATH, "//button[.//span[text()='Книги']]")
    DROPDOWN_CITY = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    DROPDOWN_CITY_MOSCOW = (By.XPATH, "//button[.//span[text()='Москва']]")
    RADIOBUTTON_NEW = (By.XPATH, "//label[text()='Новый']")

    SUBMIT_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

class UserPageLocators:
    USER_FIRST_AD = (By.XPATH, "(//div[@class='card'])[1]")
    TOP_TEXT_ON_AD = (By.XPATH, ".//h2[@class='h2' and text()='Тестовое объявление']")
    CITY_ON_AD = (By.XPATH, ".//h3[@class='h3']")
    PRICE_ON_AD = (By.XPATH, ".//div[@class='price']//h2[@class='h2']")