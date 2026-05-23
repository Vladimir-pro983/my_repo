"""Page Object для страницы логина (SauceDemo)."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы логина https://www.saucedemo.com/."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы логина.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def open(self) -> None:
        """Открыть страницу логина.

        Returns:
            None.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Войти в систему, заполнив поля и нажав кнопку Login.

        Parameters:
            username (str): имя пользователя.
            password (str): пароль.

        Returns:
            None.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
