from playwright.sync_api import Page, expect


class InventoryPage:

    INVENTORY_CONTAINER = ".inventory_list"
    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"
    ADD_TO_CART_BUTTONS = "button.btn_inventory"
    REMOVE_BUTTONS = "button:has-text('Remove')"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def __init__(self, page: Page):
        self.page = page

    def expect_visible(self):
        expect(self.page.locator(self.INVENTORY_CONTAINER)).to_be_visible()

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTONS).first.click()

    def add_items_to_cart(self, count: int):
        buttons = self.page.locator(self.ADD_TO_CART_BUTTONS)
        for i in range(count):
            buttons.nth(i).click()

    def remove_first_item_from_cart(self):
        self.page.locator(self.REMOVE_BUTTONS).first.click()

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.text_content()) if badge.is_visible() else 0

    def logout(self):
        self.page.click(self.BURGER_MENU)
        self.page.click(self.LOGOUT_LINK)
