from selenium.webdriver.common.by import By

#Поля ввода
input_name = [By.XPATH, '//input[@placeholder="* Имя"]'] #Поле ввод имени
input_surname = [By.XPATH, '//input[@placeholder="* Фамилия"]'] #Поле ввод фамилии
input_adress = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'] #Поле ввод адреса
input_metro_station = [By.XPATH, '//input[@placeholder="* Станция метро"]'] #Поле выбора станции
input_phone = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'] #Ввод телефона
input_date = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] #Поле выбора даты доставки
today = [By.CLASS_NAME, 'react-datepicker__day--today'] #Текущая дата
rental_period = [By.CLASS_NAME, 'Dropdown-placeholder'] #Поле выбора периода аренды
rental_period_choose = [By.XPATH, '//div[@class = "Dropdown-option" and text()="двое суток"]'] #Время аренды
black_color = [By.ID, 'black'] #Чекбокс черного цвета саомката

#Кнопки
button_next = [By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()= "Далее"]'] #Кнопка Далее
button_order = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()= "Заказать"]'] #Кнопка Заказать
button_yes = [By.XPATH, './/button[text()= "Да"]'] #Кнопка Да
button_status = [By.XPATH, './/button[text()= "Посмотреть статус"]'] #Кнопка Посмотреть статус

#Окно отметы заказа
button_cancel = [By.XPATH, './/button[text()= "Отменить заказ"]']
#button_look = [By.XPATH, './/button[text()= "Посмотреть"]']

#Прочее
title_completed = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'] #Заголовок "Заказ успешно оформлен"
metro_zorge_st = (By.XPATH, f'//div[text()= "Зорге"]') #Станция метро "Черкизовская"
metro_lubjanka_st = (By.XPATH, '//div[text()="Лубянка"]') #Станция метро "Курская"
