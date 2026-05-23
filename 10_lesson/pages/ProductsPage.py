"""Page Object для страницы товаров (SauceDemo)."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ProductsPage:
    """Page Object для страницы товаров (SauceDemo)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы товаров.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """Добавить товар в корзину по имени.

        Parameters:
            product_name (str): текстовое имя товара на странице
                               (например, "Sauce Labs Backpack").

        Returns:
            None.
        """
        xpath = (
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']//button"
        )
        button: WebElement = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def go_to_cart(self) -> None:
        """Перейти в корзину через значок корзины в верхнем правом углу.

        Returns:
            None.
        """
        cart_link = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
