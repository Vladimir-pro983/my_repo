import sys
from pathlib import Path

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

sys.path.insert(0, str(Path(__file__).parent.parent))


def test_shop_purchase(firefox_driver):
    """Тест покупки товаров в интернет-магазине (Firefox)"""
    # Авторизация
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров
    products_page = ProductsPage(firefox_driver)
    products_page.add_to_cart("Sauce Labs Backpack")
    products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    products_page.add_to_cart("Sauce Labs Onesie")
    products_page.go_to_cart()

    # Оформление заказа
    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    # Заполнение формы
    # Примечание: по ТЗ "Иван", "Петров", но сайт не принимает кириллицу
    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Ivan", "Petrov", "123456")

    # Проверка итоговой суммы
    total = checkout_page.get_total_price()
    expected = "58.29"
    assert total == expected, f"Ожидалась сумма ${expected}, получена ${total}"
