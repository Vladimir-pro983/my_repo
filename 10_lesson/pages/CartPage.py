"""Page Object для страницы корзины."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """Page Object для страницы корзины (страница с кнопкой Checkout)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы корзины.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def checkout(self) -> None:
        """Нажать кнопку Checkout.

        Returns:
            None.
        """
        checkout_button: WebElement = self.driver.find_element(
            By.ID, "checkout")
        checkout_button.click()
