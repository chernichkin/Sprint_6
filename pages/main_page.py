import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):

    @allure.step('Кликаем по кнопке "заказать" в центре')
    def click_on_button_order_center(self):
        self.click_on_element(MainPageLocators.button_order_center)

    def check_button_order_center_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.button_order_center)

    @allure.step('Скроллим до элемента')
    def scroll_to_button_order_center(self):
        return self.scroll_to_element(MainPageLocators.button_order_center_div)

    def check_main_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.main_title)

    def get_text_in_main_title(self):
        return self.get_text_element(MainPageLocators.main_title)

    def check_button_order_in_header_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.button_order_header)

    @allure.step('Кликаем по лого самоката')
    def click_logo(self):
        self.click_on_element(BasePageLocators.logo)

    def check_logo_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.logo)

    @allure.step('Кликаем по лого яндекса')
    def click_logo_yandex(self):
        self.click_on_element(BasePageLocators.logo_yandex)

    def check_logo_yandex_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.logo_yandex)

    @allure.step('Кликаем по кнопке заказать из хэдера')
    def click_button_order_header(self):
        self.click_on_element(BasePageLocators.button_order_header)

    @allure.step('Получаем текст открывшегося списка')
    def click_to_target_in_list(self, locator_id):
        self.click_to_target_by_id(locator_id)

    @allure.step('Получаем текст открывшегося списка')
    def get_text_in_opened_list(self, locator_id):
        self.get_text_in_target_by_id(locator_id)
