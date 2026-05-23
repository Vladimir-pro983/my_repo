"""Тесты для медленного калькулятора (slow-calculator.html)."""

import sys
from pathlib import Path

import allure

from pages.CalculatorPage import CalculatorPage

# Добавить корень проекта в PYTHONPATH, чтобы импорт pages работал
sys.path.insert(0, str(Path(__file__).parent.parent))


@allure.title("Калькулятор: сложение 7 + 8 с задержкой 45 секунд")
@allure.description(
    "Открыть страницу медленного калькулятора, установить задержку 45 секунд, "
    "ввести выражение 7+8, дождаться результата и проверить, что он равен 15."
)
@allure.feature("Calculator")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_addition(driver):
    """Тест сложения 7 + 8 = 15 с задержкой 45 секунд."""
    calc_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Ввести выражение 7 + 8 ="):
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")

    with allure.step("Ожидать появления результата 15 и получить текст"):
        calc_page.wait_for_result("15")
        result = calc_page.get_result()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Ожидался результат 15, но получен {result}"
