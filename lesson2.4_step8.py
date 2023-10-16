from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from core.utils import get_chrome


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = get_chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")            #Задаем счетчик ожидания до нужного текста
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    button_2 = browser.find_element('xpath', "//button[@type='submit']")              #находим кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)     #делаем скролл до кнопки

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button_2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()