from selenium.webdriver.common.by import By


class ProductsPage:
    """Page Object для страницы товаров"""

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        """Добавить товар в корзину по имени"""
        button = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        button.click()

    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()