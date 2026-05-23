"""Тесты для формы data-types.html."""

import sys
from pathlib import Path

import allure

from pages.FormPage import FormPage

# Добавить корень проекта в PYTHONPATH, чтобы импорт pages работал
sys.path.insert(0, str(Path(__file__).parent.parent))


@allure.title("Форма data-types: Zip с ошибкой, остальные поля успешны")
@allure.description(
    "Открыть страницу формы, заполнить все поля, отправить форму и проверить, "
    "что поле Zip code подсвечено красным (alert-danger), а остальные поля — "
    "зелёным (alert-success)."
)
@allure.feature("Form")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission_flow(driver):
    """Тест заполнения и отправки формы с проверкой валидации полей."""
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы data-types.html"):
        form_page.open()

    with allure.step("Заполнить все поля формы значениями по умолчанию"):
        form_page.fill_form()

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step(
            "Проверить, что Zip code подсвечен красным (alert-danger)"):
        assert form_page.is_zip_code_error(), (
            "Поле Zip code должно быть подсвечено красным (alert-danger)."
        )

    with allure.step(
        "Проверить, что остальные поля подсвечены зелёным (alert-success)"
    ):
        assert form_page.are_all_fields_success(), (
            "Все остальные поля должны быть подсвечены зелёным "
            "(alert-success)."
        )
