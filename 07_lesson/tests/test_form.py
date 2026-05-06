import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages.FormPage import FormPage


def test_form_submission_flow(driver):
    """Тест заполнения и отправки формы"""
    form_page = FormPage(driver)

    form_page.open()
    form_page.fill_form()
    form_page.submit_form()

    # Проверки ТОЛЬКО в тесте!
    assert form_page.is_zip_code_error(), \
        "Поле Zip code должно быть подсвечено красным"
    assert form_page.are_all_fields_success(), \
        "Все остальные поля должны быть подсвечены зелёным"