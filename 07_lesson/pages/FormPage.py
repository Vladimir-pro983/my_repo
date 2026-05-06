from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """Page Object для формы заполнения данных"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
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

    def open(self):
        """Открыть страницу формы"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    def fill_form(self):
        """Заполнить все поля формы"""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    def submit_form(self):
        """Отправить форму"""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        ).click()

    def get_field_class(self, field_id):
        """Получить класс поля по ID"""
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return element.get_attribute("class")

    def is_zip_code_error(self):
        """Проверить, есть ли ошибка в поле Zip code"""
        return "alert-danger" in self.get_field_class("zip-code")

    def are_all_fields_success(self):
        """Проверить, что все поля (кроме Zip) успешно заполнены"""
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "alert-success" not in self.get_field_class(field):
                return False
        return True