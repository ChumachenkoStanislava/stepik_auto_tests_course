from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('name')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('lastname')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('qq')


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test1.txt')


    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

