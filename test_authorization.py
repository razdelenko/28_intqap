from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from test_data import Valid_Data
from test_data import Invalid_Data
from tests.vars import PanelNavigation
from tests.vars import Autorization
from tests.vars import AutorizationAllerts
from tests.vars import Registration
import allure


fake_name = bimbo().name()
fake_email = qwerty().email()
fake_password = 123().password()

@allure.story('TP / Тесты Авторизации')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Registration.BUTTON_REGISTER)))


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()



    @allure.feature('Проверка кликабельности кнопок')
    def test_clicable_navi_bar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PanelNavigation.NAVI_BAR_LS))).click()
        assert self.driver.find_element(By.XPATH, PanelNavigation.FORM_LS)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PanelNavigation.NAVI_BAR_MAIL))).click()
        assert self.driver.find_element(By.XPATH, PanelNavigation.FORM_MAIL)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PanelNavigation.NAVI_BAR_LOGIN))).click()
        assert self.driver.find_element(By.XPATH, PanelNavigation.FORM_LOGIN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PanelNavigation.NAVI_BAR_TELEPHONE))).click()
        assert self.driver.find_element(By.XPATH, PanelNavigation.FORM_TELEPHONE)


        
    @allure.feature('Авторизяция по электронной почте (невалидные данные)')
    def test_autorization_invalid_email(self):
        self.driver.find_element(By.ID, Autorization.USER).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Autorization.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Autorization.BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.TEXT_INVALID_EMAIL)


    @allure.feature('Авторизация по номеру телефона (несуществующий)')
    def test_autorization_invalid_phoneNumber(self):
        self.driver.find_element(By.ID, Autorization.USER).send_keys(
            Invalid_Data.invalid_phoneNumber)
        self.driver.find_element(By.ID, Autorization.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Autorization.BUTTON_LOGIN).click()
        
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.TEXT_INVALID_EMAIL)


        
    @allure.feature('Авторизация по номеру телефона (несуществующий пароль)')
    def test_autorization_invalid_password(self):
        self.driver.find_element(By.ID, Autorization.USER).send_keys(
            Valid_Data.valid_phoneNumber)
        self.driver.find_element(By.ID, Autorization.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Autorization.BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, AutorizationAllerts.TEXT_INVALID_EMAIL)


        
    @allure.feature('Авторизация по логину')
    def test_autorization_xss_in_login(self):
        self.driver.find_element(By.ID, Autorization.USER).send_keys(
            Invalid_Data.xss)
        self.driver.find_element(By.ID, Autorization.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Autorization.BUTTON_LOGIN).click()
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, AutorizationAllerts.TEXT_XSS)))
