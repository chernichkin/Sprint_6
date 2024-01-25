import pytest
import allure
from selenium import webdriver
from pages.base_page import BasePage



class TestLogo:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()


    @allure.title('Проверка редиректа на "https://dzen.ru/" при клике на логотип Yandex')
    def test_logo_redirect_true(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.check_logo_yandex_is_clickable()
        base_page.click_logo_yandex()
        base_page.switch_pages()
        current_url = base_page.get_current_url()

        assert "https://dzen.ru/" in current_url


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
