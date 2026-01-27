from pages.base_page import BasePage

class InventoryPage(BasePage):
    """
    Inventory page.
    Responsibility:
    - inventory visibility
    - add / remove items
    - cart badge state
    """

    INVENTORY_CONTAINER = ".inventory_list"

    ADD_TO_CART_BUTTON = "[data-test^='add-to-cart']"
    REMOVE_BUTTON = "[data-test^='remove']"

    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    def is_inventory_visible(self):
        return self.is_visible(self.INVENTORY_CONTAINER)

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def remove_first_item_from_cart(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def get_cart_badge_count(self):
        badge = self.page.locator(self.CART_BADGE)
        if badge.is_visible():
            return int(badge.text_content())
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def add_items_to_cart(self, count: int):
        buttons = self.page.locator(self.ADD_TO_CART_BUTTON)
        for i in range(count):
            buttons.nth(i).click()
