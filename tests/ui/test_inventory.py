from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

#Test case 1
def test_inventory_is_visible_after_login(page):
    """ INVENTORY
    Risk: user cannot see product catalog
    """
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    assert inventory_page.is_inventory_visible()

#Test case 2
def test_add_item_to_cart(page):
    """
    INVENTORY
    Risk: user cannot select product
    """
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_badge_count() == 1

#Test case 3
def test_remove_item_from_cart(page):
    """
    INVENTORY
    Risk: user cannot change selected product
    """
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_first_item_to_cart()
    inventory_page.remove_first_item_from_cart()

    assert inventory_page.get_cart_badge_count() == 0

#Test case 4
def test_user_can_go_to_cart(page):
    """
    INVENTORY
    Risk: user cannot proceed to next step
    """
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    assert "cart" in page.url

def test_user_can_add_multiple_items_to_cart(page):
    """
    INVENTORY
    Nice-to-have: multiple items selection
    """
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_items_to_cart(2)

    assert inventory_page.get_cart_badge_count() == 2


