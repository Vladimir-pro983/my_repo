import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Фикстура для Chrome (для тестов формы и калькулятора)"""
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging']
    )
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")

    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура для Firefox (для теста магазина)"""
    firefox_options = FirefoxOptions()
    firefox_options.set_preference("signon.rememberSignons", False)

    # Selenium автоматически найдёт geckodriver в PATH или кэше
    browser = webdriver.Firefox(options=firefox_options)
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()
