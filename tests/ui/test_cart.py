from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def login_and_add_item(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()


def test_item_is_displayed_in_cart(page):
    """
    CART
    Risk: selected item is not saved
    """
    login_and_add_item(page)
    cart_page = CartPage(page)

    assert cart_page.get_items_count() == 1
    assert cart_page.get_first_item_name() is not None
    assert cart_page.get_first_item_price() is not None


def test_user_can_remove_item_from_cart(page):
    """
    CART
    Risk: user cannot change selection in cart
    """
    login_and_add_item(page)
    cart_page = CartPage(page)

    cart_page.remove_first_item()

    assert cart_page.get_items_count() == 0

def test_user_can_go_back_to_inventory_from_cart(page):
    """
    CART
    Risk: user stuck in cart
    """
    login_and_add_item(page)
    cart_page = CartPage(page)

    cart_page.go_back_to_inventory()

    assert "inventory" in page.url

def test_user_can_proceed_to_checkout(page):
    """
    CART
    Risk: user cannot proceed to checkout
    """
    login_and_add_item(page)
    cart_page = CartPage(page)

    cart_page.go_to_checkout()

    assert "checkout-step-one" in page.url

def test_cart_is_empty_after_removing_all_items(page):
    """
    CART
    Risk: cart state is incorrect
    """
    login_and_add_item(page)
    cart_page = CartPage(page)

    cart_page.remove_first_item()

    assert cart_page.get_items_count() == 0
