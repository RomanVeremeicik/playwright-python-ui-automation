import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from settings import STANDARD_USER, PASSWORD

#Test Case 1 
@pytest.mark.regression
def test_01_cart_persists_after_refresh(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert cart.get_items_count() == 1

    page.reload()
    assert cart.get_items_count() == 1

#Test Case 2
@pytest.mark.regression
def test_02_session_persists_on_back(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    page.go_back()
    assert "inventory" in page.url

#Test Case 3 
@pytest.mark.regression
def test_03_no_cart_access_after_logout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)
    inventory.logout()

    page.goto(f"{login.base_url}/cart.html")
    assert "cart" not in page.url



