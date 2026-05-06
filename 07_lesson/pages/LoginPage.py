from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы логина"""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу логина"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Войти в систему"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()