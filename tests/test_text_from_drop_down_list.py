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

class TestTextDropDownList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()


    @allure.title('Проверка отображения верного текста в списке в конце страницы')
    @pytest.mark.parametrize('locator,text', [*Data.locator_text])
    def test_text_from_drop_down_list_true(self, locator, text):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.check_button_order_header_is_clickable()
        main_page.scroll_to_down_main_page()
        main_page.click_to_list_target(locator)
        target_list_text = main_page.text_in_list_target(locator)

        assert target_list_text == text


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
