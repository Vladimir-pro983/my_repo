import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


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
    # Примечание: по ТЗ должны быть "Иван", "Петров", но сайт не принимает кириллицу
    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Ivan", "Petrov", "123456")

    # Проверка итоговой суммы
    total = checkout_page.get_total_price()
    assert total == "58.29", f"Ожидалась сумма $58.29, но получена ${total}"