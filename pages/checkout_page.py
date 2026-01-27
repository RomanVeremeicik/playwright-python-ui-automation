from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Checkout page.
    Responsibility:
    - filling checkout form
    - finishing order
    """

    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"

    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"

    COMPLETE_HEADER = ".complete-header"
    ERROR_MESSAGE = "[data-test='error']"
    CANCEL_BUTTON = "#cancel"

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def is_order_completed(self):
        return self.is_visible(self.COMPLETE_HEADER)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)
