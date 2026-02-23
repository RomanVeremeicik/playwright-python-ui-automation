import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from settings import STANDARD_USER, PASSWORD

#Test Case 1
@pytest.mark.regression
def test_01_inventory_visible_after_login(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.expect_visible()

#Test Case 2
@pytest.mark.regression
def test_02_add_item_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    assert inventory.get_cart_badge_count() == 1

#Test Case 3
@pytest.mark.regression
def test_03_remove_item_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.remove_first_item_from_cart()
    assert inventory.get_cart_badge_count() == 0

#Test Case 4
@pytest.mark.regression
def test_04_user_can_go_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    assert "cart" in page.url

#Test Case 5
@pytest.mark.regression
def test_05_user_can_add_multiple_items(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    inventory.add_items_to_cart(2)
    assert inventory.get_cart_badge_count() == 2


