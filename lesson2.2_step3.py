import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1')
    y = browser.find_element(By.ID, 'num2')
    z = str(int(x.text) + int(y.text))




    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(z)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
#except Exception as e:
    #print(e)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()