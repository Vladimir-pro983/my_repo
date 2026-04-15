### Поле ввода

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


def main():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("12345")
        time.sleep(1)

        input_field.clear()
        time.sleep(1)

        input_field.send_keys("54321")
        time.sleep(1)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()