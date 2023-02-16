from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'М'
    first_name_31_char = 'МуркаМуркаМуркаМуркаМуркаМуркаМ'
    last_name_1_char = 'У
    last_name_31_char = 'МуровнаМуровнаМуровнаМуровнаМур'
    password_21_char = 'asd123dsaasd123dsaasd'
    password_no_Lower = 'qwerty'
    password_9_char = 'qwerty123
    password_not_contain_digit = "Qwertyui"
    xss = '<script>qwerty(123)</script>'
    email_without_domain = 'asd123@mail.ru
    invalid_phoneNumber = '+71111111111'

class Valid_Data:
    valid_first_name = 'Диана'
    valid_last_name = 'Бабурина'
    valid_password = 'qwerty'
    valid_phoneNumber = '+7999999555'
