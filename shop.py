# #####################################################
# """Shop: отображение страницы товара"""
# ####################################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Залогиньтесь"""
#
# my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
# my_account.click() # кликнуть по My Account
# time.sleep(2)
#
# username = driver.find_element_by_id("username") # поиск поля для ввода почты или имени
# username.send_keys("mashinist81717@gmail.com") # ввод почты
# time.sleep(2)
#
# password = driver.find_element_by_id("password") # поиск поля ввода пароля
# password.send_keys("gipnofrog200489") # ввод пароля
# time.sleep(2)
#
# login_btn = driver.find_element_by_css_selector("p:nth-child(3)>input:nth-child(3)") # поиск кнопки login на странице
# login_btn.click() # нажатие на кнопку
# time.sleep(2)
#
# """ 3. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """ 4. Откройте книгу "HTML 5 Forms"""
#
# html_5 = driver.find_element_by_css_selector(".post-181>.woocommerce-LoopProduct-link") # находим карточку книги
# html_5.click() # нажимамем на нее
#
# """ 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"""
#
# header = driver.find_element_by_css_selector(".entry-summary>h1")
# header_get_title = header.text
# assert header_get_title == "HTML5 Forms"
#
# time.sleep(2)
# driver.quit()

# ################################################
# """Shop: количество товаров в категории"""
# ###############################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Залогиньтесь"""
#
# my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
# my_account.click() # кликнуть по My Account
# time.sleep(2)
#
# username = driver.find_element_by_id("username") # поиск поля для ввода почты или имени
# username.send_keys("mashinist81717@gmail.com") # ввод почты
# time.sleep(2)
#
# password = driver.find_element_by_id("password") # поиск поля ввода пароля
# password.send_keys("gipnofrog200489") # ввод пароля
# time.sleep(2)
#
# login_btn = driver.find_element_by_css_selector("p:nth-child(3)>input:nth-child(3)") # поиск кнопки login на странице
# login_btn.click() # нажатие на кнопку
# time.sleep(2)
#
# """ 3. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """ 4. Откройте категорию "HTML"""
#
# html = driver.find_element_by_css_selector(".cat-item-19>a") # находим категория HTML
# html.click() # нажимаем на нее
#
# """5. Добавьте тест, что отображается три товара"""
#
# items_count = driver.find_elements_by_css_selector(".masonry-done>li") # ищем товары на странице
# time.sleep(2)
# if len(items_count) == 3: # посчитываем количество элементов
#     print("Отображаются 3 товара")
# else:
#     print("Ошибка. Товаров: " + str(len(items_count)))
#
# driver.quit()


# ################################################
# """Shop: сортировка товаров"""
# ################################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Залогиньтесь"""
#
# my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
# my_account.click() # кликнуть по My Account
# time.sleep(2)
#
# username = driver.find_element_by_id("username") # поиск поля для ввода почты или имени
# username.send_keys("mashinist81717@gmail.com") # ввод почты
# time.sleep(2)
#
# password = driver.find_element_by_id("password") # поиск поля ввода пароля
# password.send_keys("gipnofrog200489") # ввод пароля
# time.sleep(2)
#
# login_btn = driver.find_element_by_css_selector("p:nth-child(3)>input:nth-child(3)") # поиск кнопки login на странице
# login_btn.click() # нажатие на кнопку
# time.sleep(2)
#
# """ 3. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """ 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию"""
#
# selector_default = driver.find_element_by_css_selector(".woocommerce-ordering>.orderby") # находим селектор
# selector_default_checking = selector_default.get_attribute("value") # получаем значение по умолчанию
# if selector_default_checking == "menu_order":
#     print("Селектор по умолчанию выбран верно")
# else:
#     print("Селектор по умолчанию выбран неверно")
#
# """ 5. Отсортируйте товары по цене от большей к меньшей"""
#
# sorting_selector = driver.find_element_by_css_selector(".woocommerce-ordering>.orderby") # находим селектор
# high_to_low = Select(sorting_selector) # делаем запрос к классу
# high_to_low.select_by_value("price-desc") # выбираем сортировку от большей к меньшей
#
# """ 6. Снова объявите переменную с локатором основного селектора сортировки"""
#
# sorting_selector = driver.find_element_by_css_selector(".woocommerce-ordering>.orderby") # находим селектор
#
# """ 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей"""
#
# status_selector_6 = sorting_selector.get_attribute("value") # получаем значение value
# if status_selector_6 == "price-desc": # сравниваем равно ли значение в value значению "price-desc"
#     print("Выбран вариант по цене от большей к меньшей")
# else:
#     print("Выбран неверный вариант сортировки")
# driver.quit()

# #########################################
# """Shop: отображение, скидка товара"""
# #########################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Залогиньтесь"""
#
# my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
# my_account.click() # кликнуть по My Account
# time.sleep(2)
#
# username = driver.find_element_by_id("username") # поиск поля для ввода почты или имени
# username.send_keys("mashinist81717@gmail.com") # ввод почты
# time.sleep(2)
#
# password = driver.find_element_by_id("password") # поиск поля ввода пароля
# password.send_keys("gipnofrog200489") # ввод пароля
# time.sleep(2)
#
# login_btn = driver.find_element_by_css_selector("p:nth-child(3)>input:nth-child(3)") # поиск кнопки login на странице
# login_btn.click() # нажатие на кнопку
# time.sleep(2)
#
# """ 3. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """4. Откройте книгу "Android Quick Start Guide"""
#
# android_book = driver.find_element_by_css_selector(".post-169 a:nth-child(2)") # находим карточку товара
# android_book.click() # кликаем по ней
#
# """5. Добавьте тест, что содержимое старой цены = "₹600.00"""
#
# old_price = driver.find_element_by_css_selector(".price>del>span") # находим старую цену
# old_price_text = old_price.text # получаем текст
# assert old_price_text == "₹600.00" # убеждаемся что значение соответсвтует
#
# """6. Добавьте тест, что содержимое новой цены = "₹450.00"""
#
# new_price = driver.find_element_by_css_selector(".price>ins>span")# находим новую цену
# new_price_text = new_price.text # получаем текст
# assert new_price_text == "₹450.00" # убеждаемся что значение соответсвтует
#
# """7. Добавьте явное ожидание и нажмите на обложку книги"""
#
# book_picture = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".zoom>img"))) # ждем кликабельности обложки
# book_picture.click() # нажимаем на обложку
#
# """ 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)"""
#
# close_picture = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_details a.pp_close"))) # ждем кликабельности кнопки закрытия
# close_picture.click() # нажимаем на крестик
#
# time.sleep(3)
# driver.quit()

# ###########################################
# """Shop: проверка цены в корзине"""
# ###########################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """ 3. Добавьте в корзину книгу "HTML5 WebApp Development"""
#
# add_to_basket = driver.find_element_by_css_selector(".post-182 a:nth-child(2)") # находим книгу
# add_to_basket.click() # добавляем в корзину
# time.sleep(2)
#
# """ 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"""
#
# items = driver.find_element_by_class_name("cartcontents") # находим количество товаров в корзине
# items_value = items.text # получаем текст
# assert items_value == "1 Item" # проводим проверку на совпадение текста
#
# price = driver.find_element_by_css_selector(".wpmenucart-contents span:nth-child(3)") # находим цену товаров в корзине
# price_value = price.text # получаем текст
# assert price_value == "₹180.00" # проводим проверку на совпадение текста
#
# """ 5. Перейдите в корзину"""
#
# cart = driver.find_element_by_class_name("wpmenucart-contents") # находим корзину
# cart.click() # нажимаем на нее
#
# """ 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость"""
#
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))
#
# """7. Используя явное ожидание, проверьте что в Total отобразилась стоимость"""
#
# total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total td"), "₹183.60"))
#
# driver.quit()

# ###############################################
# """Shop: работа в корзине"""
# ###############################################
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
# driver.maximize_window()
# driver.create_options()
# time.sleep(5)
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[1]
# driver.switch_to.window(first_browser_tab)
# time.sleep(5)
# driver.close()
# first_tab = driver.window_handles[0]
# driver.switch_to.window(first_tab)
#
# """ 1.Откройте https://practice.automationtesting.in/"""
#
# driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу
#
# """ 2. Нажмите на вкладку "Shop"""
#
# shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
# shop_tab.click() # нажимаем вкладку
#
# """ 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"""
#
# driver.execute_script("window.scrollBy(0, 300);") # проскроливаем страницу вниз 300 пикселей
# time.sleep(2)
# add_to_basket_1 = driver.find_element_by_css_selector(".post-182 a:nth-child(2)") # находим первую книгу
# add_to_basket_1.click() # добавляем в корзину
# time.sleep(3)
# add_to_basket_2 = driver.find_element_by_css_selector(".post-165 a:nth-child(2)") # находим вторую книгу (книга не как в инструкции из-за out of the stock)
# add_to_basket_2.click() # добавляем в корзину
#
# """ 4. Перейдите в корзину"""
#
# cart = driver.find_element_by_class_name("wpmenucart-contents") # находим корзину
# cart.click() # нажимаем на нее
#
# """ 5. Удалите первую книгу"""
#
# first_book_delete = driver.find_element_by_css_selector(".cart_item:nth-child(1)>td.product-remove>a") # ищем крестик для удаления первой книги
# first_book_delete.click() # нажимаем
#
# """6. Нажмите на Undo (отмена удаления)"""
#
# time.sleep(2)
# undo = driver.find_element_by_css_selector(".woocommerce-message>a") # находим кнопку Undo
# undo.click() # нажимаем
#
# """ 7. В Quantity увеличьте количесто товара до 3 шт для одной из книг"""
#
# java = driver.find_element_by_css_selector("tbody:nth-child(2)>tr:nth-child(1) td:nth-child(5)>div>input") # находим поле ввода для колва товара
# java.clear() # очищаем поле
# java.send_keys(3) # вводим колво 3
#
#
# """8. Нажмите на кнопку "UPDATE BASKET"""
#
# update_btn = driver.find_element_by_css_selector(".actions .button:nth-child(2)") # находим кнопку Update Basket
# update_btn.click() # нажимаем
#
# """ 9. Добавьте тест, что value элемента quantity для первой книги равно 3"""
#
# quantity_value = driver.find_element_by_css_selector("tbody:nth-child(2)>tr:nth-child(1) td:nth-child(5)>div>input") # находим поле с количеством книг
# quantity_value_check = quantity_value.get_attribute("value") # выясняем значение атрибута value
# quantity_amount = quantity_value_check # присваиваем атрибуту переменную
# time.sleep(3)
# assert quantity_amount == "3" # проверяем что value равно колву книг в поле
#
# """10. Нажмите на кнопку "APPLY COUPON """
#
# coupon_btn = driver.find_element_by_css_selector(".coupon .button") # ищем кнопку для использования купона
# time.sleep(3)
# coupon_btn.click() # нажимаем на кнопку
#
# """11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."""
#
# message = driver.find_element_by_class_name("woocommerce-error")
# message_check = message.text
# assert message_check == "Please enter a coupon code."
# time.sleep(3)
#
# driver.quit()

#######################################################
"""Shop: покупка товара"""
#######################################################

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
driver.maximize_window()
driver.create_options()
time.sleep(5)
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[1]
driver.switch_to.window(first_browser_tab)
time.sleep(5)
driver.close()
first_tab = driver.window_handles[0]
driver.switch_to.window(first_tab)

""" 1.Откройте https://practice.automationtesting.in/"""

driver.get("https://practice.automationtesting.in/") # переходим на стартовую страницу

""" 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз"""

shop_tab = driver.find_element_by_css_selector("#menu-item-40>a") # находим вкладку Shop
shop_tab.click() # нажимаем вкладку
driver.execute_script("window.scrollBy(0, 300);") # проскроливаем на 300 пикселей вниз

""" 3. Добавьте в корзину книгу "HTML5 WebApp Development"""

add_to_basket = driver.find_element_by_css_selector(".post-182 a:nth-child(2)") # находим книгу
add_to_basket.click() # добавляем в корзину

""" 4. Перейдите в корзину"""

time.sleep(3)
cart = driver.find_element_by_class_name("wpmenucart-contents") # находим корзину
cart.click() # нажимаем на нее

""" 5. Нажмите "PROCEED TO CHECKOUT"""

checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))) # явное ожидание для кнопки Proceed to checkout
checkout_btn.click() # нажимаем на кнопку

""" 6. Заполните все обязательные поля"""

first_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name"))) # явное ожидание пере заполнением поля first name
first_name.send_keys("Jimmy") # заполняем имя
last_name = driver.find_element_by_id("billing_last_name") # находим last_name
last_name.send_keys("Carter") # заполняем
email = driver.find_element_by_id("billing_email") # находим почту
email.send_keys("goose_palmate@gmail.com") # заполняем
phone = driver.find_element_by_id("billing_phone") # находим номер телефона
phone.send_keys("1234567890") # заполняем
country = driver.find_element_by_id("s2id_billing_country") # находим страну
country.click() # кликаем по селектору
search = driver.find_element_by_id("s2id_autogen1_search") # осуществляем поиск поля ввода
search.send_keys("Rus") # вводим данные
country_choice = driver.find_element_by_css_selector(".select2-result-selectable.select2-highlighted") # находим один из найденных вариантов
country_choice.click() # выбираем
address = driver.find_element_by_css_selector("input#billing_address_1") # находим поле для адреса
address.send_keys("51 Goose srt 98") # заполняем
town = driver.find_element_by_css_selector("input#billing_city") # находим поле для города
town.send_keys("Minsk") # заполняем
state = driver.find_element_by_css_selector("input#billing_state") # находим поле для региона
state.send_keys("Minsk") # заполняем
postal_code = driver.find_element_by_css_selector("input#billing_postcode") # находим поле для почтового кода
postal_code.send_keys("117293") # заполняем

""" 7. Выберите способ оплаты "Check Payments"""

driver.execute_script("window.scrollBy(0, 600);") # проскроливаем на 600 пикселей вниз
time.sleep(3)
payment_manner = driver.find_element_by_id("payment_method_cheque") # находим чек бокс с нужным вариантом
payment_manner.click() # нажимаем на чекбокс

""" 8. Нажмите PLACE ORDER"""

order_btn = driver.find_element_by_id("place_order") # поиск кнопки
order_btn.click() # нажатие на кнопку

""" 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."""

message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((
    By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

"""10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"""

method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "tr:nth-child(3)>td"), "Check Payments"))

time.sleep(3)

driver.quit()






