"""Page Object для страницы медленного калькулятора."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для калькулятора со страницы slow-calculator.html."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы калькулятора.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открыть страницу калькулятора.

        Returns:
            None.
        """
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url += "slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, seconds: int) -> None:
        """Установить задержку в секундах в поле #delay.

        Parameters:
            seconds (int): значение задержки в секундах.

        Returns:
            None.
        """
        delay_field: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def press_button(self, button_text: str) -> None:
        """Нажать кнопку калькулятора по тексту на кнопке.

        Parameters:
            button_text (str): текст кнопки (например, "7", "+", "=").

        Returns:
            None.
        """
        button: WebElement = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()

    def get_result(self) -> str:
        """Получить текст с экрана калькулятора.

        Returns:
            str: текст результата с элемента .screen.
        """
        screen: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, ".screen")
        return screen.text

    def wait_for_result(self, expected_result: str) -> None:
        """Дождаться, пока на экране появится заданный результат.

        Parameters:
            expected_result (str): ожидаемый текст результата.

        Returns:
            None.
        """
        screen_locator = (By.CSS_SELECTOR, ".screen")
        self.wait.until(
            EC.text_to_be_present_in_element(
                screen_locator, expected_result
            )
        )
