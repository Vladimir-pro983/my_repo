from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_fields_validation():
    """
    Тест проверяет валидацию полей формы:
    - Zip code должно быть красным (невалидное)
    - Остальные поля должны быть зелеными (валидные)
    """

    # Инициализация драйвера Edge
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 15)

        # Ждем загрузки формы
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # Шаг 2: Заполнить форму - используем поиск по name атрибуту

        # First name
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        first_name.clear()
        first_name.send_keys("Иван")

        # Last name
        last_name = driver.find_element(By.NAME, "last-name")
        last_name.clear()
        last_name.send_keys("Петров")

        # Address
        address = driver.find_element(By.NAME, "address")
        address.clear()
        address.send_keys("Ленина, 55-3")

        # E-mail
        email = driver.find_element(By.NAME, "e-mail")
        email.clear()
        email.send_keys("test@skypro.com")

        # Phone number
        phone = driver.find_element(By.NAME, "phone")
        phone.clear()
        phone.send_keys("+7985899998787")

        # Zip code - оставляем пустым
        zip_code = driver.find_element(By.NAME, "zip-code")
        zip_code.clear()

        # City
        city = driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("Москва")

        # Country
        country = driver.find_element(By.NAME, "country")
        country.clear()
        country.send_keys("Россия")

        # Job position
        job_position = driver.find_element(By.NAME, "job-position")
        job_position.clear()
        job_position.send_keys("QA")

        # Company
        company = driver.find_element(By.NAME, "company")
        company.clear()
        company.send_keys("SkyPro")

        print("✓ Форма заполнена")

        # Шаг 3: Нажать кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Ждем появления элемента с ID на странице результата
        wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Шаг 4: Проверка цветов полей на странице результата

        # Проверяем Zip code - должен быть красным (alert-danger)
        zip_code_result = driver.find_element(By.ID, "zip-code")
        zip_code_bg = zip_code_result.value_of_css_property("background-color")

        print(f"Zip code background: {zip_code_bg}")

        # Bootstrap использует #f8d7da для ошибок, что в RGB: rgba(248, 215, 218, 1)
        assert "248, 215, 218" in zip_code_bg or "rgba(248, 215, 218" in zip_code_bg, \
            f"Zip code должно быть красным (248, 215, 218), но цвет: {zip_code_bg}"

        print(f"✓ Zip code подсвечено красным")

        # Шаг 5: Проверка остальных полей - должны быть зелеными (alert-success)
        # Bootstrap использует #d1e7dd для успеха, что в RGB: rgba(209, 231, 221, 1)

        green_fields = {
            "First name": driver.find_element(By.ID, "first-name"),
            "Last name": driver.find_element(By.ID, "last-name"),
            "Address": driver.find_element(By.ID, "address"),
            "E-mail": driver.find_element(By.ID, "e-mail"),
            "Phone number": driver.find_element(By.ID, "phone"),
            "City": driver.find_element(By.ID, "city"),
            "Country": driver.find_element(By.ID, "country"),
            "Job position": driver.find_element(By.ID, "job-position"),
            "Company": driver.find_element(By.ID, "company")
        }

        for field_name, field_element in green_fields.items():
            field_bg = field_element.value_of_css_property("background-color")

            print(f"{field_name} background: {field_bg}")

            assert "209, 231, 221" in field_bg or "rgba(209, 231, 221" in field_bg, \
                f"{field_name} должно быть зеленым (209, 231, 221), но цвет: {field_bg}"

            print(f"✓ {field_name} подсвечено зеленым")

        print("\n✅ Все проверки пройдены успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        # Сохраняем скриншот для отладки
        driver.save_screenshot("error_screenshot.png")
        print("Скриншот сохранен: error_screenshot.png")

        # Выводим текущий URL
        print(f"Текущий URL: {driver.current_url}")

        # Выводим информацию о всех элементах с классом alert
        try:
            alerts = driver.find_elements(By.CSS_SELECTOR, "[class*='alert']")
            print(f"\nНайдено элементов с alert: {len(alerts)}")
            for idx, alert in enumerate(alerts):
                alert_id = alert.get_attribute("id")
                alert_class = alert.get_attribute("class")
                alert_bg = alert.value_of_css_property("background-color")
                print(f"  [{idx}] id='{alert_id}', class='{alert_class}', bg={alert_bg}")
        except:
            pass

        raise

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_form_fields_validation()