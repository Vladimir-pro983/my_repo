"""Тест сценария покупки товаров в интернет-магазине SauceDemo (Firefox)."""

import sys
from pathlib import Path

import allure

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

# Добавить корень проекта в PYTHONPATH, чтобы импорт pages работал
sys.path.insert(0, str(Path(__file__).parent.parent))


@allure.title("Покупка нескольких товаров в SauceDemo (Firefox)")
@allure.description(
    "Авторизоваться под стандартным пользователем, добавить несколько товаров "
    "в корзину,"
    " оформить заказ и проверить итоговую сумму на странице Checkout."
)
@allure.feature("Shopping")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase(firefox_driver):
    """Тест покупки нескольких товаров в интернет-магазине SauceDemo."""
    with allure.step("Авторизоваться под пользователем standard_user"):
        login_page = LoginPage(firefox_driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step(
        "Добавить в корзину товары:"
        " Backpack, Bolt T-Shirt, Onesie и перейти в корзину"
    ):
        products_page = ProductsPage(firefox_driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_to_cart("Sauce Labs Onesie")
        products_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа (Checkout)"):
        cart_page = CartPage(firefox_driver)
        cart_page.checkout()

    with allure.step("Заполнить форму доставки на странице Checkout"):
        # Примечание: сайт не принимает кириллицу, поэтому используем латиницу
        checkout_page = CheckoutPage(firefox_driver)
        checkout_page.fill_form("Ivan", "Petrov", "123456")

    with allure.step("Проверить итоговую сумму заказа"):
        total = checkout_page.get_total_price()
        expected = "58.29"
        assert total == expected, (
            f"Ожидалась сумма ${expected}, получена ${total}"
        )
