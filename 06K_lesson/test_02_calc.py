from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_with_delay():
    """
    Тест проверяет работу калькулятора с задержкой:
    - Устанавливает задержку 45 секунд
    - Выполняет операцию 7 + 8
    - Проверяет, что результат 15 появляется через 45 секунд
    """

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Шаг 1: Открыть страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Ждем загрузки поля задержки
        delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))

        # Шаг 2: Установить задержку 45 секунд
        delay_input.clear()
        delay_input.send_keys("45")

        print("✓ Задержка установлена: 45 секунд")

        # Шаг 3: Нажать кнопки калькулятора: 7 + 8 =

        # Нажать кнопку "7"
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()
        print("✓ Нажата кнопка: 7")

        # Нажать кнопку "+"
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()
        print("✓ Нажата кнопка: +")

        # Нажать кнопку "8"
        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        print("✓ Нажата кнопка: 8")

        # Нажать кнопку "="
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()
        print("✓ Нажата кнопка: =")
        print("⏳ Ожидание результата (45 секунд)...")

        # Шаг 4: Ждем результат 15 в течение 46 секунд
        # Используем явное ожидание с таймаутом чуть больше 45 секунд
        wait_result = WebDriverWait(driver, 46)

        # Ждем, пока в экране калькулятора появится текст "15"
        result_screen = wait_result.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                "15"
            )
        )

        # Проверяем результат
        screen = driver.find_element(By.CLASS_NAME, "screen")
        result_text = screen.text

        print(f"✓ Результат получен: {result_text}")

        # Шаг 5: Проверка (assert), что результат равен 15
        assert result_text == "15", f"Ожидался результат '15', но получен '{result_text}'"

        print("\n✅ Тест пройден успешно! Результат 7 + 8 = 15")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        # Сохраняем скриншот для отладки
        driver.save_screenshot("calc_error_screenshot.png")
        print("Скриншот сохранен: calc_error_screenshot.png")
        raise

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_calculator_with_delay()