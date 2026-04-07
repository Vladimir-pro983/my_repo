import pytest
from string_utils import StringUtils


su = StringUtils()


# ===== capitalize =====

def test_capitalize_simple_word():
    # позитивный: обычное слово с маленькой буквы
    assert su.capitalize("skypro") == "Skypro"


def test_capitalize_already_capitalized():
    # позитивный: уже с заглавной буквы
    assert su.capitalize("Skypro") == "Skypro"


def test_capitalize_empty_string():
    # негативный: пустая строка
    assert su.capitalize("") == ""


def test_capitalize_none_raises_error():
    # негативный: None как строка -> ожидаем AttributeError
    with pytest.raises(AttributeError):
        su.capitalize(None)


# ===== trim =====

def test_trim_leading_spaces():
    # позитивный: удаляем пробелы в начале
    assert su.trim("   skypro") == "skypro"


def test_trim_no_leading_spaces():
    # позитивный: строка без пробелов в начале не меняется
    assert su.trim("skypro") == "skypro"


def test_trim_only_spaces():
    # негативный: только пробелы -> полностью очищаем
    assert su.trim("   ") == ""


def test_trim_none_raises_error():
    # негативный: None как строка -> ожидаем AttributeError
    with pytest.raises(AttributeError):
        su.trim(None)


# ===== contains =====

def test_contains_true_when_symbol_present():
    # позитивный
    assert su.contains("SkyPro", "S") is True


def test_contains_false_when_symbol_absent():
    # позитивный
    assert su.contains("SkyPro", "U") is False


def test_contains_empty_symbol():
    # негативный: пустая строка как symbol
    # string.index("") всегда возвращает 0, так что метод вернёт True
    assert su.contains("SkyPro", "") is True


def test_contains_in_empty_string():
    # негативный: поиск в пустой строке
    assert su.contains("", "S") is False


def test_contains_none_string_raises_error():
    # негативный: None как строка -> ожидаем AttributeError
    with pytest.raises(AttributeError):
        su.contains(None, "S")


# ===== delete_symbol =====

def test_delete_symbol_one_char():
    # позитивный: удаляем одиночный символ
    assert su.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    # позитивный: удаляем подстроку
    assert su.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    # негативный: символа/подстроки нет – строка без изменений
    assert su.delete_symbol("SkyPro", "XYZ") == "SkyPro"


def test_delete_symbol_empty_symbol():
    # негативный: пустая строка как symbol
    # string.replace("", "") вернет исходную строку
    assert su.delete_symbol("SkyPro", "") == "SkyPro"