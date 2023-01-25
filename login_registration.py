# ####################################################
# """Registration_login: регистрация аккаунта"""
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
# """ 2. Нажмите на вкладку "My Account"""
#
# my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
# my_account.click() # кликнуть по My Account
# time.sleep(3)
#
# """ 3. В разделе "Register", введите email для регистрации"""
#
# email = driver.find_element_by_id("reg_email") # поиск поля почты для заполнения
# email.send_keys("mashinist81717@gmail.com") # ввод email
# time.sleep(3)
#
# """ 4. В разделе "Register", введите пароль для регистрации"""
#
# password = driver.find_element_by_id("reg_password") # поиск поля для ввода пароля
# password.send_keys("gipnofrog200489") # ввод пароля
# time.sleep(3)
#
# """ 5. Нажмите на кнопку "Register"""
#
# register_btn = driver.find_element_by_css_selector(".woocomerce-FormRow input:nth-child(3)") # поиск кнопки Register
# register_btn.click() # нажатие на кнопку
#
# time.sleep(5)
# driver.quit()


###############################################
"""Registration_login: логин в систему"""
###############################################

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path_to_extension = r'C:\Users\79689\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options) # команда драйвера переписана для блокировки рекламы и установки ад блокера
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

""" 2. Нажмите на вкладку "My Account"""

my_account = driver.find_element_by_css_selector("#menu-item-50>a") # поиск My Account
my_account.click() # кликнуть по My Account
time.sleep(2)

""" 3. В разделе "Login", введите email для логина"""

username = driver.find_element_by_id("username") # поиск поля для ввода почты или имени
username.send_keys("mashinist81717@gmail.com") # ввод почты
time.sleep(2)

"""4. В разделе "Login", введите пароль для логина"""

password = driver.find_element_by_id("password") # поиск поля ввода пароля
password.send_keys("gipnofrog200489") # ввод пароля
time.sleep(2)

""" 5. Нажмите на кнопку "Login"""

login_btn = driver.find_element_by_css_selector("p:nth-child(3)>input:nth-child(3)") # поиск кнопки login на странице
login_btn.click() # нажатие на кнопку
time.sleep(2)

"""6. Добавьте проверку, что на странице есть элемент "Logout"""

element = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout a") # нашли элемент по составному селектору
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "Logout" # проверили название элемента

time.sleep(3)
driver.quit()


