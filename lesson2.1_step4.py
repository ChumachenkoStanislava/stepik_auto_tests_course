from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    option = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()