import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_user_can_complete_checkout(page):
    """
    CHECKOUT
    Risk: user cannot complete purchase
    End-to-end happy path
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # login
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # select product
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # cart -> checkout
    cart_page.go_to_checkout()

    # checkout step one
    checkout_page.fill_checkout_form(
        first_name="John",
        last_name="Doe",
        postal_code="12345"
    )
    checkout_page.continue_checkout()

    # finish
    checkout_page.finish_checkout()

    assert checkout_page.is_order_completed()

@pytest.mark.parametrize(
    "first_name,last_name,postal_code",
    [
        ("", "Doe", "12345"),     # missing first name
        ("John", "", "12345"),    # missing last name
        ("John", "Doe", ""),      # missing postal code
    ]
)
def test_checkout_required_fields_validation(
    page, first_name, last_name, postal_code
):
    """
    CHECKOUT
    Risk: order can be created with missing mandatory data
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # login
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # add product
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # go to checkout
    cart_page.go_to_checkout()

    # fill incomplete form
    checkout_page.fill_checkout_form(
        first_name=first_name,
        last_name=last_name,
        postal_code=postal_code
    )
    checkout_page.continue_checkout()

    assert checkout_page.is_error_displayed()

def test_cancel_checkout_returns_user_to_cart(page):
    """
    CHECKOUT
    Nice-to-have: cancel checkout flow
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()

    checkout_page.cancel_checkout()

    assert "cart" in page.url

def test_checkout_with_multiple_items(page):
    """
    CHECKOUT
    Nice-to-have: checkout with multiple items
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_items_to_cart(2)
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()

    checkout_page.fill_checkout_form(
        first_name="Jane",
        last_name="Doe",
        postal_code="54321"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.is_order_completed()

