from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        """Заполнить форму данных"""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        # Ждём, что кнопка станет кликабельной
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def get_total_price(self):
        """Получить итоговую стоимость"""
        # Ждём появления элемента с итоговой суммой
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        # Формат: "Total: $58.29"
        total_text = total_element.text
        return total_text.replace("Total: $", "")
