import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from settings import STANDARD_USER, PASSWORD

#Test Case 1
@pytest.mark.smoke
def test_01_login_success(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)

    assert "inventory" in page.url

#Test Case 2
@pytest.mark.regression
def test_02_login_invalid_password(page):
    login = LoginPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, "wrong_password")

    login.expect_error_visible()
    assert "inventory" not in page.url

#Test Case 3
@pytest.mark.regression
def test_03_login_locked_user(page):
    login = LoginPage(page)

    login.open_login_page()
    login.login("locked_out_user", PASSWORD)

    login.expect_error_visible()
    assert "inventory" not in page.url

#Test Case 4
@pytest.mark.regression
def test_04_login_empty_credentials(page):
    login = LoginPage(page)

    login.open_login_page()
    login.login("", "")

    login.expect_error_visible()

#Test Case 5
@pytest.mark.regression
def test_05_direct_inventory_access_without_login(page):
    login = LoginPage(page)

    page.goto(f"{login.base_url}/inventory.html")
    assert "inventory" not in page.url

#Test Case 6
@pytest.mark.regression
def test_06_access_denied_after_logout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)
    inventory.logout()

    page.goto(f"{login.base_url}/inventory.html")
    assert "inventory" not in page.url


