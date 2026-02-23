import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from settings import STANDARD_USER, PASSWORD

#Test Case 1
@pytest.mark.regression
def test_01_complete_checkout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.go_to_checkout()
    checkout.fill_checkout_form("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.is_order_completed()


@pytest.mark.regression
@pytest.mark.parametrize(
    "first,last,postal",
    [
        ("", "Doe", "12345"),
        ("John", "", "12345"),
        ("John", "Doe", ""),
    ],
)
#Test Case 2
def test_02_required_fields_validation(page, first, last, postal):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.go_to_checkout()
    checkout.fill_checkout_form(first, last, postal)
    checkout.continue_checkout()
    assert checkout.is_error_displayed()

#Test Case 3
@pytest.mark.regression
def test_03_cancel_checkout_returns_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.go_to_checkout()
    checkout.cancel_checkout()

    assert "cart" in page.url

#Test Case 4
@pytest.mark.regression
def test_04_checkout_multiple_items(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_items_to_cart(2)
    inventory.go_to_cart()

    cart.go_to_checkout()
    checkout.fill_checkout_form("Jane", "Doe", "54321")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.is_order_completed()

