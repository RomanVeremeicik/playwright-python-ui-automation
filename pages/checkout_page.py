from playwright.sync_api import Page, expect

class CheckoutPage:

    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"
    SUCCESS_MESSAGE = ".complete-header"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        self.page = page

    # Основной метод
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    # Wrapper для тестов
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.fill_checkout_information(first_name, last_name, postal_code)

    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)

    def cancel_checkout(self):
        self.page.click(self.CANCEL_BUTTON)

    def expect_success_message(self):
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_be_visible()

    def expect_error_visible(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
