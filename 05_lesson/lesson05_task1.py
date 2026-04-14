### Клик по кнопке с CSS-классом

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://uitestingplayground.com/classattr")

        wait = WebDriverWait(driver, 10)
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )

        button.click()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()