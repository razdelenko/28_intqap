class Autorization():
    USER = 'username'
    PASSWORD = "password"
    LOGIN = "kc-login"
    BUTTON_REGISTER = "kc-register"
    BUTTON_LOGIN = "kc-login"

class Registration:
    BUTTON_REGISTER = "kc-register"
    FIRSTNAME = "//input[@name='firstName']"
    LASTNAME = "//input[@name='lastName']"
    NUMBER_OR_EMAIL = "address"
    PASSWORD = "password"
    PASSWORD_CONFIRM = "password-confirm"
    BUTTON_SUBMIT = "//button[@type='submit']"
    ENTER_CODE = "rt-code-1"

class RegistrationsAllerts:
    ALLERTS_ERROR = "//span[@class='rt-input-container__meta rt-input-container__meta--error']"

class PanelNavigation:
    NAVI_BAR_TELEPHONE = '//*[@id="t-btn-tab-phone"]'
    FORM_TELEPHONE = "//span[contains(text(), 'Мобильный телефон')]"
    NAVI_BAR_MAIL = '//*[@id="t-btn-tab-mail"]'
    FORM_MAIL = "//span[contains(text(), 'Электронная почта')]"
    NAVI_BAR_LOGIN = '//*[@id="t-btn-tab-login"]'
    FORM_LOGIN = "//span[contains(text(), 'Логин')]"
    NAVI_BAR_LS = '//*[@id="t-btn-tab-ls"]'
    FORM_LS = "//span[contains(text(), 'Лицевой счёт')]"

class AutorizationAllerts:
    ALLERTS_ERROR = '//*[@id="form-error-message"]'
    TEXT_INVALID_EMAIL = "//span[contains(text(), 'Неверный логин или пароль')]"
    TEXT_XSS = "//h2[contains(text(), 'Ваш запрос был отклонен из соображений безопасности.')]"
