
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
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        wait = WebDriverWait(driver, 20)

        third_image = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
        )

        src_value = third_image.get_attribute("src")
        print(src_value)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
