import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages.CalculatorPage import CalculatorPage


def test_calculator_addition(driver):
    """Тест сложения 7 + 8 = 15 с задержкой 45 секунд"""
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay(45)

    calc_page.press_button("7")
    calc_page.press_button("+")
    calc_page.press_button("8")
    calc_page.press_button("=")

    calc_page.wait_for_result("15")
    result = calc_page.get_result()

    assert result == "15", f"Ожидался результат 15, но получен {result}"