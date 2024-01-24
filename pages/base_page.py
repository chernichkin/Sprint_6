import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element(*BasePageLocators.logo).click()

    def click_button_order_header(self):
        self.driver.find_element(*BasePageLocators.button_order_header).click()
