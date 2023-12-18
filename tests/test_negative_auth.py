# Тесты группы "Авторизация. Негативные тесты" - вход в ЛК
# Проверка авторизации с пустым телефоном/e-mail/логином/ЛС
# Проверка авторизации с правильным телефоном/e-mail/логином/ЛС и пустым паролем
# Ввод некорректного номера телефона
# Ввод некорректного e-mail
# Вход с верным телефоном/e-mail/логином/ЛС и неверным паролем
# Вход с неверным телефоном/e-mail/логином/ЛС и верным паролем

import time
import pytest
from pages.auth_page import AuthPage
from pages.setting import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome('C:/projects/Skillfactory/chromedriver.exe')

@pytest.mark.parametrize('phone', ['', ' '], ids= ['Empty phone', 'Space phone'])
def test_auth_by_empty_phone(phone, web_browser):
    """ Тест-кейс SF-AT-006: попытка авторизации с пустым номером телефона """

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    assert link_lk not in web_browser.current_url, f'SF-AT-006 failed: Выполнен вход в ЛК'
    time.sleep(10)
    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите номер телефона', 'SF-AT-006 failed: нет предупреждения о пустом номере телефона'
    time.sleep(10)


@pytest.mark.parametrize('email', ['', ' '], ids=['Empty email', 'Space email'])
def test_auth_by_empty_email(email, web_browser):
    """ Тест-кейс SF-AT-011: попытка авторизации с пустым адресом электронной почты """

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Введите адрес, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR,
                                    'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите адрес, указанный при регистрации', f'SF-AT-011 failed: нет предупреждения о пустом e-mail'
    time.sleep(10)


@pytest.mark.parametrize('login', ['', ' '], ids= ['Empty login', 'Space login'])
def test_auth_by_empty_login(login, web_browser):
    """ Тест-кейс SF-AT-016: попытка авторизации с пустым логином """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_login)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(login)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(20)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Введите логин, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите логин, указанный при регистрации', f'SF-AT-016 failed: нет предупреждения о пустом логине'
    time.sleep(10)

@pytest.mark.parametrize('ls', ['', ' '], ids= ['Empty ls', 'Space ls'])
def test_auth_by_empty_ls(ls, web_browser):
    """ Тест-кейс SF-AT-018: попытка авторизации с пустым ЛС """

    page = AuthPage(web_browser)

    # Переходим на таб Логин
    page.swich_tab(page.tab_ls)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(ls)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Введите номер вашего лицевого счета"
    assert web_browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите номер вашего лицевого счета', f'SF-AT-018 failed: нет предупреждения о пустом ЛС'
    time.sleep(10)

@pytest.mark.parametrize('username, password, test_num', [
                            (valid_phone, '', 'SF-AT-007'),
                            (valid_phone, ' ', 'SF-AT-007'),
                            (valid_email, '', 'SF-AT-012'),
                            (valid_email, ' ', 'SF-AT-012'),
                            (valid_login, '', 'SF-AT-017'),
                            (valid_login, ' ', 'SF-AT-017'),
                            (valid_ls, '', 'SF-AT-019'),
                            (valid_ls, ' ', 'SF-AT-019')
                        ], ids= [
                            'Phone: Empty password',
                            'Phone: Space password',
                            'Email: Empty password',
                            'Email: Space password',
                            'Login: Empty password',
                            'Login: Space password',
                            'LS: Empty password',
                            'LS: Space password'
                        ])
@pytest.mark.xfail(reason='Нереализовано')
def test_auth_by_username_and_empty_password(username, password, test_num, web_browser):
    """ Тест-кейс SF-AT-007/SF-AT-012/SF-AT-017/SF-AT-019: попытка авторизации с пустым паролем """

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Введите пароль"
    assert web_browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите пароль', f"{test_num} failed: Нет вывода сообщения 'Введите пароль'"
    time.sleep(10)

@pytest.mark.parametrize('username, test_num', [
                                ('+7(000)0000000', 'SF-AT-008'),
                                ('lolkek@gmail.com', 'SF-AT-014')
                            ], ids= [
                                'Wrong phone number',
                                'Wrong email'
                            ]
                         )
def test_auth_by_wrong_phone(username, test_num, web_browser):
    """ Тест-кейс SF-AT-008/SF-AT-014: попытка авторизации неверным username и верным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        print('Captcha')
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', f"{test_num} failed: Нет надписи 'Неверный логин или пароль'"
    time.sleep(10)

@pytest.mark.parametrize('username, password, test_num', [
                            (valid_phone, 'dhsfgds741', 'SF-AT-009'),
                            (valid_email, 'khghdg789', 'SF-AT-013'),
                        ], ids= [
                            'Phone: Wrong password',
                            'Email: Wrong password',
                        ])
def test_auth_by_wrong_password(username, password, test_num, web_browser):
    """ Тест-кейс SF-AT-009 и SF-AT-013: попытка авторизации верным username и неверным паролем"""

    page = AuthPage(web_browser)

    # Вводим логин/пароль
    page.enter_username(username)
    page.enter_pass(password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        print("Captcha")
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()
    time.sleep(10)

    # Появляется надпись "Неверный логин или пароль"
    assert web_browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', f"{test_num} failed: Нет надписи 'Неверный логин или пароль'"
    time.sleep(10)

@pytest.mark.parametrize('phone', ['+7(654)741852'], ids= ['Not correct numb'])
def test_auth_by_bad_format_phone(phone, web_browser):
    """ Тест-кейс SF-AT-010: попытка авторизации по номеру телефона в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Мобильный телефон
    page.swich_tab(page.tab_phone)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(phone)
    page.enter_pass(valid_password)

    # Если есть капча, ставим задержку для ввода капчи
    if page.captcha:
        time.sleep(15)

    # Нажимаем кнопку "Войти"
    page.btn_click()

    # Появляется надпись "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Неверный формат телефона', f"SF-AT-010 failed: Нет надписи 'Неверный логин или пароль'"
    time.sleep(10)


@pytest.mark.parametrize('email', ['lol2kek@gmail.cm'], ids= ['Not correct email'])
def test_auth_by_bad_format_email(email, web_browser):
    """ Тест-кейс SF-AT-015: попытка авторизации по e-mail в неверном формате"""

    page = AuthPage(web_browser)

    # Переходим на таб Почта
    page.swich_tab(page.tab_email)
    print(page.title_username.text)

    # Вводим логин/пароль
    page.enter_username(email)
    page.enter_pass(valid_password)

    # Проверка перехода на таб "Логин"
    assert web_browser.find_element(By.CSS_SELECTOR, 'div.rt-tab.rt-tab--small.rt-tab--active').text == 'Логин', f"SF-AT-015 failed: не перешли на таб 'Логин'"
    time.sleep(10)

    #python -m pytest -v --driver Chrome --driver-path C:/projects/Skillfactory/chromedriver.exe tests/test_negative_auth.py