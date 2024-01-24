import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators as Opl

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.driver.find_element(*Opl.name).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.driver.find_element(*Opl.surname).send_keys(surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.driver.find_element(*Opl.address).send_keys(address)

    def click_metro_station(self):
        self.driver.find_element(*Opl.metro_station).click()

    def click_metro_zorge_st(self):
        self.driver.find_element(*Opl.metro_zorge_st).click()

    def click_metro_lubjanka_st(self):
        self.driver.find_element(*Opl.metro_lubjanka_st).click()

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
        self.driver.find_element(*Opl.phone).send_keys(phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        self.driver.find_element(*Opl.button_next).click()

    def check_button_next(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(Opl.button_next))


    def click_date(self):
        self.driver.find_element(*Opl.date).click()

    def click_today(self):
        self.driver.find_element(*Opl.today).click()

    @allure.step('Выбираем дату')
    def set_date(self):
        self.click_date()
        self.click_today()

    def click_rental_period(self):
        self.driver.find_element(*Opl.rental_period).click()

    def click_rental_period_choose(self):
        self.driver.find_element(*Opl.rental_period_choose).click()

    @allure.step('Выбираем дни аренды')
    def set_rental_period(self):
        self.click_rental_period()
        self.click_rental_period_choose()

    @allure.step('Выбираем цвет')
    def click_black_color(self):
        self.driver.find_element(*Opl.black_color).click()

    def check_button_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(Opl.button_order))

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_button_order(self):
        self.driver.find_element(*Opl.button_order).click()

    def check_button_yes_is_clickable(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(Opl.button_yes))

    @allure.step('Кликаем на кнопку "Да"')
    def click_button_yes(self):
        self.driver.find_element(*Opl.button_yes).click()

    def check_visibility_of_button_status(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Opl.button_status))

    def click_button_status(self):
        self.driver.find_element(*Opl.button_status).click()

    def check_button_cancel(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(Opl.button_cancel))

    @allure.step('Получаем текст кнопки "проверить статус"')
    def text_in_button_status(self):
        return self.driver.find_element(*Opl.button_status).text

