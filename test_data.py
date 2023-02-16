from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'Р'
    first_name_31_char = 'РоманРоманРоманРоманРоманРоманР'
    last_name_1_char = 'К'
    last_name_31_char = 'КольцовКольцовКольцовКольцовКол'
    password_21_char = '123qwertyqwertyqwerty'
    password_no_Lower = 'qwerty'
    password_9_char = 'qwerty123
    password_not_contain_digit = 'Qwertyuiop'
    xss = '<script>alert(123)</script>'
    email_without_domain = 'abc123@mail'
    invalid_phoneNumber = '+71111111111'

class Valid_Data:
    valid_first_name = 'Роман'
    valid_last_name = 'Кольцов'
    valid_password = 'Qwerty36'
    valid_phoneNumber = '+77081095251'
