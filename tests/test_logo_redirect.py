import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка редиректа на "https://dzen.ru/" при клике на логотип Yandex')
    def test_logo_redirect_true(self, driver):
        main_page = MainPage(driver)
        main_page.check_logo_yandex_is_clickable()
        main_page.click_logo_yandex()
        main_page.switch_pages()
        current_url = main_page.get_current_url()

        assert "https://dzen.ru/" in current_url

