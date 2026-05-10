from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для калькулятора"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора"""
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url += "slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, seconds):
        """Установить задержку в секундах"""
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def press_button(self, button_text):
        """Нажать кнопку калькулятора по тексту"""
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()

    def get_result(self):
        """Получить результат с экрана калькулятора"""
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text

    def wait_for_result(self, expected_result):
        """Дождаться появления результата на экране"""
        screen_locator = (By.CSS_SELECTOR, ".screen")
        self.wait.until(
            EC.text_to_be_present_in_element(
                screen_locator, str(expected_result)
            )
        )
