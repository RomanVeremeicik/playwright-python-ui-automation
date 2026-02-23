from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def expect_not_empty(self):
        expect(self.cart_items).not_to_have_count(0)

    def proceed_to_checkout(self):
        self.checkout_button.click()
