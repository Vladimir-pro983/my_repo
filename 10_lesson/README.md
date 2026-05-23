# 10_lesson — PageObject + Allure

Набор автотестов для веб‑страниц с использованием Selenium и Pattern Page Object.  
Отчёты формируются через Allure.

---

## Описание проекта

- PageObject‑классы:  
  `CalculatorPage`, `FormPage`, `LoginPage`, `ProductsPage`, `CartPage`, `CheckoutPage`.
- Тесты запускаются через `pytest` и генерируют Allure‑отчёт.
- Для проверки стиля кода используется `flake8`.

---

## Как запустить тесты для формирования отчёта

1. Установить зависимости:

   ```bash
   pip install -r 10_lesson/requirements.txt
   ```

   В `requirements.txt` должны быть, как минимум:

   ```text
   pytest
   allure-pytest
   selenium
   webdriver-manager
   flake8
   ```

2. Запустить тесты и сохранить результаты Allure:

   ```bash
   python -m pytest --alluredir=10_lesson/allure-results 10_lesson/tests/
   ```

---

## Как просмотреть сформированный отчёт

1. Включить сервер и открыть отчёт в браузере:

   ```bash
   allure serve 10_lesson/allure-results
   ```

2. Или сгенерировать статический HTML‑отчёт:

   ```bash
   allure generate 10_lesson/allure-results -o 10_lesson/allure-report --clean
   ```

   После этого открой в браузере файл:

   ```bash
   10_lesson/allure-report/index.html
   ```

---

## Важно

- Папки `10_lesson/allure-results/` и `10_lesson/allure-report/` **не пушить в Git**:
  - добавь в `.gitignore`:

    ```text
    10_lesson/allure-results/
    10_lesson/allure-report/
    ```

- Перед сдачей задания проверь стиль кода:

  ```bash
  python -m flake8 10_lesson
  ```

  Если команда ничего не выводит — всё ок.