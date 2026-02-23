from playwright.sync_api import Page, expect


class CheckoutPage:

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page: Page):
        self.page = page

    def fill_checkout_information(self, first: str, last: str, zip_code: str):
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)

    def cancel_checkout(self):
        self.page.click(self.CANCEL_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()

    def expect_checkout_complete(self):
        expect(self.page.locator(self.COMPLETE_HEADER)).to_be_visible()
