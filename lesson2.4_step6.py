from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)

    button = browser.find_element(By.ID, "button")
    button.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()