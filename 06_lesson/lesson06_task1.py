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
        driver.get("http://uitestingplayground.com/ajax")

        wait = WebDriverWait(driver, 20)

        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )
        button.click()

        message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='content']//p")
            )
        )

        print(message.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()