from playwright.sync_api import Page, expect


class CartPage:

    CART_ITEM = ".cart_item"
    REMOVE_BUTTON = "button:has-text('Remove')"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"

    def __init__(self, page: Page):
        self.page = page

    # Количество товаров
    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    # Удалить первый товар
    def remove_first_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    # Удалить все товары
    def remove_all_items(self):
        buttons = self.page.locator(self.REMOVE_BUTTON)
        while buttons.count() > 0:
            buttons.first.click()

    # Перейти к checkout
    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    # Вернуться в inventory
    def go_back_to_inventory(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)

    # Проверка что корзина пуста
    def expect_cart_empty(self):
        expect(self.page.locator(self.CART_ITEM)).to_have_count(0)
