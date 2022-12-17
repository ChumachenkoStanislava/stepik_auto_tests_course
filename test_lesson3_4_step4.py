import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()



class Test_forfeedBack():
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])
    def test_for_feed_back(self, browser, links):
        link = links
        browser.get(link)
        time.sleep(5)

        input = browser.find_element(By.TAG_NAME, "textarea")
        input.send_keys(math.log(int(time.time()+0.015)))
        time.sleep(3)

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        confirmation = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        x = confirmation.text

        assert "Correct!" == x, "* wrong number entered *"




if __name__ == "__main__":
    pytest.main()