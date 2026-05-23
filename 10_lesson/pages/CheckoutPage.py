"""Page Object для страницы оформления заказа."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа (Checkout)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы Checkout.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """Заполнить форму данных доставки и нажать кнопку Continue.

        Parameters:
            first_name (str): имя пользователя.
            last_name (str): фамилия пользователя.
            postal_code (str): почтовый индекс.

        Returns:
            None.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        # Ждём, что кнопка станет кликабельной и нажимаем её
        continue_button: WebElement = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def get_total_price(self) -> str:
        """Получить итоговую стоимость из строки Total.

        Returns:
            str: числовая часть суммы без "Total: $" (например, "58.29").
        """
        # Ждём появления элемента с итоговой суммой
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )

        total_text = total_element.text
        return total_text.replace("Total: $", "")
