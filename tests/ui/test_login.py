from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# === GATE 1: AUTHENTICATION ===
# Test_Case 1
def test_p0_login_success(page):
    """Risk: user cannot login"""
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

# Test_Case 2
def test_p0_login_invalid_password(page):
    """Risk: unauthorized access"""
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "wrong_password")

    assert login_page.is_error_displayed()
    assert "inventory" not in page.url

# Test_Case 3
def test_p0_login_locked_user(page):
    """Risk: blocked users can access system"""
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed()
    assert "inventory" not in page.url

# Test_Case 4
def test_p0_login_empty_credentials(page):
    """Risk: invalid input not handled"""
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("", "")

    assert login_page.is_error_displayed()

# Test_Case 5
def test_p0_direct_inventory_access_without_login(page):
    """Risk: unauthorized access via direct URL"""
    page.goto("https://www.saucedemo.com/inventory.html")

    assert "inventory" not in page.url

# Test_Case 6
def test_p0_access_denied_after_logout(page):
    """Risk: session not cleared after logout"""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.logout()

    page.goto("https://www.saucedemo.com/inventory.html")

    assert "inventory" not in page.url


