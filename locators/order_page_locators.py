from selenium.webdriver.common.by import By

input_name = [By.XPATH, '//input[@placeholder="* Имя"]']
input_surname = [By.XPATH, '//input[@placeholder="* Фамилия"]']
input_adress = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
input_metro_station = [By.XPATH, '//input[@placeholder="* Станция метро"]']


metro_zorge_st = (By.XPATH, '//div[text()="Зорге"]') # Станция метро "Черкизовская"
metro_lubjanka_st = (By.XPATH, '//div[text()="Лубянка"]') # Станция метро "Курская"
