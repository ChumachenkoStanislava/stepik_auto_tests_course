from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


class Test_input(unittest.TestCase):
    def test_input1(self):
        input1 = browser.find_element('xpath', "//input[@placeholder='Input your name']")
        input1.send_keys("Ivan")

    def test_input3(self):
        input3 = browser.find_element('xpath', "//input[@placeholder='Input your email']")
        input3.send_keys("qqq@mail.ru")

    def test_input4(self):
        button = browser.find_element('xpath', "//button[@class='btn btn-default']")
        button.click()

    def test_input5(self):
        confirmation = browser.find_element(By.TAG_NAME, 'h1')
        x = confirmation.text
        self.assertEqual('Congratulations! You have successfully registered!', x, " * Registration failed * ")


if __name__ == "__main__":
    unittest.main()

