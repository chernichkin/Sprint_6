from selenium.webdriver.common.by import By

class OrderPageLocators:
    #Поля ввода
    name = [By.XPATH, '//input[@placeholder="* Имя"]'] #Поле ввод имени
    surname = [By.XPATH, '//input[@placeholder="* Фамилия"]'] #Поле ввод фамилии
    address = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'] #Поле ввод адреса
    metro_station = [By.XPATH, '//input[@placeholder="* Станция метро"]'] #Поле выбора станции
    phone = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'] #Ввод телефона
    date = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] #Поле выбора даты доставки
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

    #Прочее
    metro_zorge_st = (By.XPATH, f'//div[text()= "Зорге"]') #Станция метро "Черкизовская"
    metro_lubjanka_st = (By.XPATH, '//div[text()="Лубянка"]') #Станция метро "Курская"
