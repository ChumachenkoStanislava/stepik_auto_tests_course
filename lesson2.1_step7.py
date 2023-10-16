from selenium.webdriver.common.by import By
import time
import math
from core.utils import get_chrome

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = get_chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    chest = browser.find_element(By.ID, 'treasure')
    chest_x = chest.get_attribute('valuex')
    x = chest_x
    y = calc(x)


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