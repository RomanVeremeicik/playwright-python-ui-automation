"""
Smoke tests:
Critical go / no-go user flows.
If any test fails -> release is blocked.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_smoke_login_success(page):
    """
    AUTH
    Risk: user cannot access system
    """
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_smoke_logout_blocks_access(page):
    """
    AUTH
    Risk: unauthorized access after logout
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.logout()

    page.goto("https://www.saucedemo.com/inventory.html")

    assert "inventory" not in page.url


def test_smoke_inventory_visible(page):
    """
    INVENTORY
    Risk: product catalog not available
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_inventory_visible()


def test_smoke_add_item_to_cart(page):
    """
    INVENTORY
    Risk: user cannot select product
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_badge_count() == 1


def test_smoke_item_present_in_cart(page):
    """
    CART
    Risk: selected product is lost
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.get_items_count() == 1


def test_smoke_go_to_checkout(page):
    """
    CART
    Risk: user cannot proceed to checkout
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()

    assert "checkout-step-one" in page.url


def test_smoke_checkout_happy_path(page):
    """
    CHECKOUT
    Risk: user cannot complete purchase
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

    checkout_page.fill_checkout_form(
        first_name="John",
        last_name="Doe",
        postal_code="12345"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.is_order_completed()


def test_smoke_cart_empty_after_checkout(page):
    """
    CHECKOUT
    Risk: cart state is inconsistent after order completion
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

    checkout_page.fill_checkout_form(
        first_name="Jane",
        last_name="Doe",
        postal_code="54321"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    inventory_page.go_to_cart()

    assert cart_page.get_items_count() == 0


