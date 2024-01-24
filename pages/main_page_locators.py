import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element(*MainPageLocators.button_order_center).click()

    def check_button_order_center_is_enabled(self):
        return self.driver.find_element(*MainPageLocators.button_order_center).is_enabled()
