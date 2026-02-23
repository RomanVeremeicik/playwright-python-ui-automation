from playwright.sync_api import Page, expect


class CartPage:

    CART_ITEM = ".cart_item"
    REMOVE_BUTTON = "button:has-text('Remove')"
    CONTINUE_SHOPPING = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page):
        self.page = page

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def remove_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def remove_all_items(self):
        buttons = self.page.locator(self.REMOVE_BUTTON)
        while buttons.count() > 0:
            buttons.first.click()

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING)

    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    def expect_cart_empty(self):
        expect(self.page.locator(self.CART_ITEM)).to_have_count(0)
