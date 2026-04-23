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
        driver.get("http://uitestingplayground.com/textinput")

        wait = WebDriverWait(driver, 10)

        input_field = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='text']")
            )
        )
        input_field.clear()
        input_field.send_keys("SkyPro")

        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        button.click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "button.btn-primary"),
                "SkyPro"
            )
        )

        button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print(button.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()