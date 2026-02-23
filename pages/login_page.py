from playwright.sync_api import Page, expect
from settings import BASE_URL

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open_login_page(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()

    def expect_error_visible(self):
        expect(self.page.locator(self.error_message)).to_be_visible()
