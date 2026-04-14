### Форма авторизации

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Инициализация Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # 1. Открыть страницу логина
        driver.get("http://the-internet.herokuapp.com/login")

        # Явные ожидания, чтобы элементы успели загрузиться
        wait = WebDriverWait(driver, 10)

        # 2. Ввести username
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_input.send_keys("tomsmith")

        # 3. Ввести password
        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys("SuperSecretPassword!")

        # 4. Нажать кнопку Login
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()

        # 5. Дождаться зеленой плашки и вывести её текст
        flash = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        print(flash.text.strip())

    finally:
        # 6. Закрыть браузер
        driver.quit()


if __name__ == "__main__":
    main()