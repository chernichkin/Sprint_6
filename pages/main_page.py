import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке "заказать" в центре')
    def click_button_order_center(self):
        self.driver.find_element(*MainPageLocators.button_order_center).click()

    def check_button_order_center_is_clickable(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.button_order_center))

    @allure.step('Скроллим до элемента')
    def scroll_to_button_order_center(self):
        element = self.driver.find_element(*MainPageLocators.button_order_center_div)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скроллим вниз страницы')
    def scroll_to_down_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_to_list_target(self, param):
        self.driver.find_element(By.ID, param).click()

    @allure.step('Получаем текст открывшегося списка')
    def text_in_list_target(self, param):
        return self.driver.find_element(By.ID, param).text

    def check_main_title_is_visible(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.main_title))

    def text_in_main_title(self):
        return self.driver.find_element(*MainPageLocators.main_title).text
