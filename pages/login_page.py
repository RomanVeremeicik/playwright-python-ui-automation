from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from settings import BASE_URL


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_error_visible(self):
        expect(self.error_message).to_be_visible()

    def get_error_text(self) -> str:
        return self.error_message.text_content()
