import pytest
import allure
from selenium import webdriver
from pages.base_page import BasePage


class TestLogo:

    @allure.title('Проверка редиректа на "https://dzen.ru/" при клике на логотип Yandex')
    def test_logo_redirect_true(self, driver):
        base_page = BasePage(driver)
        base_page.check_logo_yandex_is_clickable()
        base_page.click_logo_yandex()
        base_page.switch_pages()
        current_url = base_page.get_current_url()

        assert "https://dzen.ru/" in current_url

