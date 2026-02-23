import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from settings import STANDARD_USER, PASSWORD


@pytest.mark.smoke
def test_01_login_success(page):
    login = LoginPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    assert "inventory" in page.url


@pytest.mark.smoke
def test_02_inventory_page_visible(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.expect_visible()


@pytest.mark.smoke
def test_03_add_item_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert cart.get_items_count() == 1


@pytest.mark.smoke
def test_04_proceed_to_checkout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    cart.go_to_checkout()

    assert "checkout-step-one" in page.url


@pytest.mark.smoke
def test_05_complete_checkout(page):
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


@pytest.mark.smoke
def test_06_logout_blocks_inventory_access(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.logout()

    page.goto(f"{login.base_url}/inventory.html")
    assert "inventory" not in page.url

