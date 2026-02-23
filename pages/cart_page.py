from playwright.sync_api import Page, expect

class CartPage:

    CART_ITEM = ".cart_item"
    REMOVE_BUTTON = "button:has-text('Remove')"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"

    def __init__(self, page: Page):
        self.page = page

    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def get_first_item_name(self) -> str:
        return self.page.locator(self.ITEM_NAME).first.text_content()

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def remove_all_items(self):
        buttons = self.page.locator(self.REMOVE_BUTTON)
        while buttons.count() > 0:
            buttons.first.click()

    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    def go_back_to_inventory(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)

    def expect_cart_empty(self):
        expect(self.page.locator(self.CART_ITEM)).to_have_count(0)

    def get_first_item_price(self) -> str:
        return self.page.locator(self.ITEM_PRICE).first.text_content()
         
