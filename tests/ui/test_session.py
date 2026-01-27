from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_cart_persists_after_page_refresh(page):
    """
    SESSION
    Risk: cart state is lost after page refresh
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # login
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # add item and go to cart
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.get_items_count() == 1

    # refresh page
    page.reload()

    assert cart_page.get_items_count() == 1

def test_session_persists_on_browser_back(page):
    """
    SESSION
    Risk: session breaks on browser back navigation
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # login
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # go to cart
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # browser back
    page.go_back()

    # user should still be logged in and see inventory
    assert "inventory" in page.url

def test_no_cart_access_after_logout(page):
    """
    SESSION
    Risk: unauthorized cart access after logout
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # login
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # logout
    inventory_page.logout()

    # direct access to cart
    page.goto("https://www.saucedemo.com/cart.html")

    assert "cart" not in page.url



