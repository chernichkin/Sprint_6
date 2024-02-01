import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators as Opl
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.set_field_by_locator(Opl.name, name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.set_field_by_locator(Opl.surname, surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.set_field_by_locator(Opl.address, address)

    @allure.step('Кликаем по полю "метро"')
    def click_metro_station(self):
        self.click_on_element(Opl.metro_station)

    @allure.step('Кликаем по станции "Зорге"')
    def click_metro_zorge_st(self):
        self.click_on_element(Opl.metro_zorge_st)

    @allure.step('Кликаем по станции "Лубянка"')
    def click_metro_lubjanka_st(self):
        self.click_on_element(Opl.metro_lubjanka_st)

    @allure.step('Выбираем метро')
    def set_metro_zorge_station(self):
        self.click_metro_station()
        self.click_metro_zorge_st()

    @allure.step('Выбираем метро')
    def set_metro_lubjanka_station(self):
        self.click_metro_station()
        self.click_metro_lubjanka_st()

    @allure.step('Вводим телефон')
    def set_phone(self, phone):
        self.set_field_by_locator(Opl.phone, phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        self.click_on_element(Opl.button_next)

    @allure.step('Проверяем кликабельность кнопки "далее"')
    def check_button_next(self):
        self.check_element_is_clickable(Opl.button_next)

    @allure.step('Кликаем по полю с датой')
    def click_date(self):
        self.click_on_element(Opl.date)

    @allure.step('Кликаем по сегодняшней дате')
    def click_today(self):
        self.click_on_element(Opl.today)

    @allure.step('Выбираем дату')
    def set_date(self):
        self.click_date()
        self.click_today()

    @allure.step('Кликаем по полю периода')
    def click_rental_period(self):
        self.click_on_element(Opl.rental_period)

    @allure.step('Кликаем по датам выбора аренды')
    def click_rental_period_choose(self):
        self.click_on_element(Opl.rental_period_choose)

    @allure.step('Выбираем дни аренды')
    def set_rental_period(self):
        self.click_rental_period()
        self.click_rental_period_choose()

    @allure.step('Выбираем цвет')
    def click_black_color(self):
        self.click_on_element(Opl.black_color)

    @allure.step('Проверяем кликабельность кнопки заказа')
    def check_button_order(self):
        self.check_element_is_clickable(Opl.button_order)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_button_order(self):
        self.click_on_element(Opl.button_order)

    @allure.step('Проверяем кликабельность кнопки "Да"')
    def check_button_yes_is_clickable(self):
        self.check_element_is_clickable(Opl.button_yes)

    @allure.step('Кликаем на кнопку "Да"')
    def click_button_yes(self):
        self.click_on_element(Opl.button_yes)

    @allure.step('Проверяем видимость кнопки проверки статуса')
    def check_visibility_of_button_status(self):
        self.check_element_is_visable(Opl.button_status)

    @allure.step('Кликаем по кнопке "проверить статус"')
    def click_button_status(self):
        self.click_on_element(Opl.button_status)

    @allure.step('Проверяем кликабельность кнопки отмены')
    def check_button_cancel(self):
        self.check_element_is_clickable(Opl.button_cancel)

    @allure.step('Получаем текст кнопки "проверить статус"')
    def text_in_button_status(self):
        return self.get_text_element(Opl.button_status)
