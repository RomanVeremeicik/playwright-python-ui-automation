from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.inventory_list = page.locator(".inventory_list")
        self.add_to_cart_buttons = page.locator("button[data-test^='add-to-cart']")
        self.cart_link = page.locator(".shopping_cart_link")
        self.title = page.locator(".title")

    def expect_loaded(self):
        expect(self.inventory_list).to_be_visible()

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def open_cart(self):
        self.cart_link.click()

    def expect_title(self, expected: str):
        expect(self.title).to_have_text(expected)
