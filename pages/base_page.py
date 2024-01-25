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

    @allure.step('Кликаем по лого')
    def click_logo(self):
        self.driver.find_element(*BasePageLocators.logo).click()

    def check_button_order_header_is_clickable(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(BasePageLocators.button_order_header))

    @allure.step('Кликаем по кнопке заказать из хэдера')
    def click_button_order_header(self):
        self.driver.find_element(*BasePageLocators.button_order_header).click()
