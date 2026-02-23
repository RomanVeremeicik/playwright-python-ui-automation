import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from settings import STANDARD_USER, PASSWORD

#Test Case 1
@pytest.mark.regression
def test_01_item_displayed_in_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert cart.get_items_count() == 1
    assert cart.get_first_item_name() is not None
    assert cart.get_first_item_price() is not None

#Test Case 2
@pytest.mark.regression
def test_02_remove_item_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.remove_first_item()
    assert cart.get_items_count() == 0

#Test Case 3
@pytest.mark.regression
def test_03_go_back_to_inventory(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.go_back_to_inventory()
    assert "inventory" in page.url

#Test Case 4
@pytest.mark.regression
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

#Test Case 5
@pytest.mark.regression
def test_05_cart_empty_after_removing_all(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart.remove_first_item()
    assert cart.get_items_count() == 0
