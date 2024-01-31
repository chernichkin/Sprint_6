import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from pages.base_page import BasePage
from data import Data
from pages.main_page import MainPage

class TestOrder:


    @allure.title('Проверка закакза при переходе с хэдера')
    @allure.description('Проверяем что при успешном заказе появляется всплывающее окно с кнопкой "Проверить статус"')
    @pytest.mark.parametrize('name,surname,address,phone', [*Data.order_data])
    def test_order_true(self, driver, name, surname, address, phone):

        base_page = BasePage(driver)
        base_page.check_button_order_header_is_clickable()
        base_page.click_button_order_header()
        order_page = OrderPage(driver)
        order_page.check_button_next()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro_lubjanka_station()
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.check_button_order()
        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_color()
        order_page.click_button_order()
        order_page.check_button_yes_is_clickable()
        order_page.click_button_yes()
        text_in_button = order_page.text_in_button_status()
        assert text_in_button == 'Посмотреть статус'


    @allure.title('Проверка закакза при переходе с центральной конпки')
    @allure.description('Проверяем что при успешном заказе появляется всплывающее окно с кнопкой "Проверить статус"')
    @pytest.mark.parametrize('name,surname,address,phone', [*Data.order_data])
    def test_order_from_central_button_true(self, driver, name, surname, address, phone):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        base_page = BasePage(driver)

        base_page.check_button_order_header_is_clickable()
        main_page.scroll_to_button_order_center()
        main_page.check_button_order_center_is_clickable()
        main_page.click_button_order_center()
        order_page.check_button_next()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro_lubjanka_station()
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.check_button_order()
        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_color()
        order_page.click_button_order()
        order_page.check_button_yes_is_clickable()
        order_page.click_button_yes()
        text_in_button = order_page.text_in_button_status()
        assert text_in_button == 'Посмотреть статус'

    @allure.title('Проверка возврата на главную страницу при тапе на лого самоката')
    @pytest.mark.parametrize('name,surname,address,phone', [*Data.order_data])
    def test_back_to_main_page(self, driver, name, surname, address, phone):

        driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(driver)
        base_page.check_button_order_header_is_clickable()
        base_page.click_button_order_header()
        order_page = OrderPage(driver)
        order_page.check_button_next()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro_lubjanka_station()
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.check_button_order()
        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_color()
        order_page.click_button_order()
        order_page.check_button_yes_is_clickable()
        order_page.click_button_yes()
        order_page.click_button_status()
        base_page.check_logo_is_clickable()
        base_page.click_logo()
        main_page = MainPage(driver)
        main_page.check_main_title_is_visible()
        text_in_title = main_page.text_in_main_title()

        assert 'Самокат' in text_in_title
