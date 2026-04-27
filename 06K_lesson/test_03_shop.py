from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    """
    Тест проверяет процесс покупки в интернет-магазине:
    - Авторизация пользователя
    - Добавление товаров в корзину
    - Оформление заказа
    - Проверка итоговой суммы
    """

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Переменная для хранения итоговой стоимости
    total_price = None

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Шаг 2: Авторизация как standard_user
        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        print("✓ Авторизация выполнена")

        # Ждем загрузки страницы с товарами
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Шаг 3: Добавить товары в корзину

        # Sauce Labs Backpack
        backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_button.click()
        print("✓ Добавлен товар: Sauce Labs Backpack")

        # Sauce Labs Bolt T-Shirt
        tshirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_button.click()
        print("✓ Добавлен товар: Sauce Labs Bolt T-Shirt")

        # Sauce Labs Onesie
        onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_button.click()
        print("✓ Добавлен товар: Sauce Labs Onesie")

        # Шаг 4: Перейти в корзину
        cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
        print("✓ Переход в корзину")

        # Ждем загрузки корзины
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))

        # Шаг 5: Нажать Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        print("✓ Нажата кнопка Checkout")

        # Ждем загрузки формы
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        # Шаг 6: Заполнить форму данными
        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")

        print("✓ Форма заполнена")

        # Шаг 7: Нажать кнопку Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        print("✓ Нажата кнопка Continue")

        # Ждем загрузки страницы с итоговой информацией
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))

        # Шаг 8: Прочитать итоговую стоимость (Total)
        total_label = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_price = total_label.text

        print(f"✓ Итоговая стоимость: {total_price}")

        # Шаг 9: Закрыть браузер
        driver.quit()
        print("✓ Браузер закрыт")

        # Шаг 10: Проверка, что итоговая сумма равна $58.29
        # Извлекаем числовое значение из текста "Total: $58.29"
        assert total_price == "Total: $58.29", \
            f"Ожидалась сумма 'Total: $58.29', но получена '{total_price}'"

        print("\n✅ Тест пройден успешно! Итоговая сумма: $58.29")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        # Сохраняем скриншот для отладки
        driver.save_screenshot("shop_error_screenshot.png")
        print("Скриншот сохранен: shop_error_screenshot.png")

        # Выводим текущий URL для отладки
        print(f"Текущий URL: {driver.current_url}")

        # Закрываем браузер в случае ошибки
        driver.quit()
        raise


if __name__ == "__main__":
    test_shop_purchase()