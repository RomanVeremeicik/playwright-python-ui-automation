from pages.base_page import BasePage

class CartPage(BasePage):
    """
    Cart page.
    Responsibility:
    - view selected items
    - remove items
    - navigation (back / checkout)
    """

    CART_ITEM = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CART_ITEM_PRICE = ".inventory_item_price"

    REMOVE_BUTTON = "[data-test^='remove']"
    BACK_TO_INVENTORY_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"

    def get_items_count(self):
        return self.page.locator(self.CART_ITEM).count()

    def get_first_item_name(self):
        return self.page.locator(self.CART_ITEM_NAME).first.text_content()

    def get_first_item_price(self):
        return self.page.locator(self.CART_ITEM_PRICE).first.text_content()

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def go_back_to_inventory(self):
        self.click(self.BACK_TO_INVENTORY_BUTTON)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
