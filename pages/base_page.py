import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по лого самоката')
    def click_logo(self):
        self.driver.find_element(*BasePageLocators.logo).click()

    def check_logo_is_clickable(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(BasePageLocators.logo))

    @allure.step('Кликаем по лого яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*BasePageLocators.logo_yandex).click()

    def check_logo_yandex_is_clickable(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(BasePageLocators.logo_yandex))

    def check_button_order_header_is_clickable(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(BasePageLocators.button_order_header))

    @allure.step('Кликаем по кнопке заказать из хэдера')
    def click_button_order_header(self):
        self.driver.find_element(*BasePageLocators.button_order_header).click()

    @allure.step('Смена страниц')
    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url
