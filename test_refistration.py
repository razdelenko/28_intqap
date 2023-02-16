from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from test_data import Valid_Data
from test_data import Invalid_Data
from tests.vars import Registration
from tests.vars import RegistrationsAllerts
import allure


fake_name = bimbo().name()
fake_email = qwerty().email()
fake_password = 123().password()

@allure.story('TP-6645 / Тесты Регистрации на RT')
class TestValidRegistration:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Registration.BUTTON_REGISTER)))
        self.driver.find_element(By.ID, Registration.BUTTON_REGISTER).click()


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

    def test_eto_baza(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.ID, Registration.ENTER_CODE)

        
    @allure.feature('Регистрация с паролем из 21 символа и более')
    def test_registration_user_with_pass_21char(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по E-mail или номеру телефона (невалидные данные)')
    def test_registration_user_with_email_without_domain(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.email_without_domain)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (имя 31 и более символов)')
    def test_registration_user_with_firstname_31char(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Invalid_Data.first_name_31_char)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (имя 1 символ)')
    def test_registration_user_with_firstname_1char(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Invalid_Data.first_name_1_char)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (пустое поле E-mail или номер телефона)')
    def test_registration_user_with_not_filled_email_or_mobile(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регитрация по номеру телефона (пустое поле Фамилия)')
    def test_registration_user_with_not_filled_lastname(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (пустое поле Имя)')
    def test_registration_user_with_not_filled_firstname(self):
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (разные данные подверждающего пароля с паролем)')
    def test_registration_user_with_non_matching_passwords(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Valid_Data.valid_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (невалидные данные пароля)')
    def test_registration_user_with_password_not_contain_digit(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)


    @allure.feature('Регистрация по номеру телефона (Фамилия 31 и более символов)')
    def test_registration_user_with_lastname_31char(self):
        self.driver.find_element(By.XPATH, Registration.FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, Registration.LASTNAME).send_keys(
            Invalid_Data.last_name_31_char)
        self.driver.find_element(By.ID, Registration.NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, Registration.PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, Registration.PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, Registration.BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RegistrationsAllerts.ALLERTS_ERROR)
