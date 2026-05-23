"""Page Object для формы заполнения данных (data-types.html)."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """Page Object для формы заполнения данных (data-types.html)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы формы.

        Parameters:
            driver (WebDriver): экземпляр веб‑драйвера.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        # Поля формы и их значения по умолчанию
        self.fields: dict = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self) -> None:
        """Открыть страницу формы.

        Returns:
            None.
        """
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        url += "data-types.html"
        self.driver.get(url)

    def fill_form(self) -> None:
        """Заполнить все поля формы значениями из словаря self.fields.

        Returns:
            None.
        """
        for field, value in self.fields.items():
            field_element: WebElement = self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            )
            field_element.send_keys(value)

    def submit_form(self) -> None:
        """Отправить форму (нажать кнопку Submit)."""
        submit_button: WebElement = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        )
        submit_button.click()

    def get_field_class(self, field_id: str) -> str:
        """Получить значение атрибута class поля по его ID.

        Parameters:
            field_id (str): ID поля (например, "first-name", "zip-code").

        Returns:
            str: значение атрибута class элемента.
        """
        element: WebElement = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return element.get_attribute("class") or ""

    def is_zip_code_error(self) -> bool:
        """Проверить, есть ли ошибка в поле Zip code (класс alert-danger).

        Returns:
            bool: True, если поле zip-code имеет класс alert-danger.
        """
        field_class = self.get_field_class("zip-code")
        return "alert-danger" in field_class

    def are_all_fields_success(self) -> bool:
        """
        Проверить, что все поля (кроме Zip code)
         успешно заполнены (класс alert-success).

        Returns:
            bool: True, если все проверяемые поля имеют класс alert-success.
        """
        fields = [
            'first-name',
            'last-name',
            'address',
            'e-mail',
            'phone',
            'city',
            'country',
            'job-position',
            'company'
        ]
        for field in fields:
            field_class = self.get_field_class(field)
            if "alert-success" not in field_class:
                return False

        return True
