from selenium.webdriver.common.by import By


class BasePageLocators:
    logo = [By.XPATH, '//img[@alt="Scooter"]']  # Логотип scooter
    logo_yandex = [By.XPATH, '//img[@alt="Yandex"]'] #Логотип яндекс
    button_order_header = [By.XPATH,
                           '//div[@class="Header_Nav__AGCXC"]/button[text()= "Заказать"]']  #Заказать из хэдера
