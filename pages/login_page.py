from playwright.sync_api import Page, expect
from settings import BASE_URL


class LoginPage:

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

    def open_login_page(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).text_content()

    def expect_error_visible(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
