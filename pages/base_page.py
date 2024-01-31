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

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    def check_element_is_visable(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скроллим вниз страницы')
    def scroll_to_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_to_target_by_id(self, locator_id):
        self.driver.find_element(By.ID, locator_id).click()

    def get_text_in_target_by_id(self, locator_id):
        return self.driver.find_element(By.ID, locator_id).text

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Смена страниц')
    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    def set_field_by_locator(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)
