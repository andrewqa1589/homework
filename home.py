###########################################
"""Home: добавление комментария"""
###########################################

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

""" 2. Проскролльте страницу вниз на 600 пикселей"""

time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);") # проскроливаем страницу вниз 600 пикселей

""" 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"""

time.sleep(3)
selenium_ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 img") # поиск кликабельного элемента для книги Selenium Ruby
selenium_ruby.click() # нажатие на элемент

""" 4. Нажмите на вкладку "REVIEWS"""

time.sleep(3)
reviews_tab = driver.find_element_by_css_selector(".reviews_tab>a") # поиск эелемента Reviews на странице
reviews_tab.click() #нажатие на элемент

""" 5. Поставьте 5 звёзд"""

time.sleep(3)
fifth_star = driver.find_element_by_css_selector(".stars a:nth-child(5)") # поиск селектора пятой звезды
fifth_star.click() # нажатие на пятую звезду

""" 6. Заполните поле "Review" сообщением: "Nice book!"""

time.sleep(3)
comment = driver.find_element_by_id("comment") # поиск поля для комментария на странице
comment.send_keys("Nice book!") # заполнение поля комментарием

""" 7. Заполните поле "Name"""

time.sleep(3)
name = driver.find_element_by_id("author")# поиск поля для введения имени
name.send_keys("Jimmy")# вводим имя

""" 8. Заполните "Email"""

time.sleep(3)
email = driver.find_element_by_id("email") # поиск поля для почты
email.send_keys("goose_palmate@gmail.com") # ввод адреса почты

""" 9. Нажмите на кнопку "SUBMIT"""

time.sleep(3)
submit_btn = driver.find_element_by_css_selector(".form-submit #submit") # поиск селектора кнопки
submit_btn.click() # нажатие на кнопку

time.sleep(5)
driver.quit()









