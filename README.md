Локаторы:
 - base_page_locators - общие локаторы из хэдера
 - main_page_locators - локаторы с главной страницы
 - order_page_locators - локаторы со страницы ввода данных и подтверждения
Страницы:
 - base_page - общие методы
 - main_page - методы главной страницы
 - order_page - методы страницы заказа
Тесты:
 - test_logo_redirect
   - test_logo_redirect_true - 'Проверка редиректа на "https://dzen.ru/" при клике на логотип Yandex'
 - test_order_page
   - test_order_true - 'Проверка закакза при переходе с хэдера'
   - test_order_from_central_button_true - 'Проверка закакза при переходе с центральной конпки'
   - test_order_true - 'Проверка возврата на главную страницу при тапе на лого самоката'
 - test_text_from_drop_down_list
   - test_text_from_drop_down_list_true - 'Проверка отображения верного текста в списке в конце страницы'
Данные для параметризации в data.py