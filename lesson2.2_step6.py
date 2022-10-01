from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script('window.scrollBy(0, 80);')
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    option = browser.find_element(By.ID, 'robotCheckbox')
    option.click()
    option1 = browser.find_element(By.ID, 'robotsRule')
    option1.click()
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


