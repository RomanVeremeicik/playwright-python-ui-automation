from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_LIST = ".inventory_list"
    TITLE = ".title"

    def is_inventory_loaded(self):
        self.expect_visible(self.INVENTORY_LIST)

    def get_title(self):
        return self.get_text(self.TITLE)
