from playwright.sync_api import Page
from pages.base_page import BasePage
from settings import BASE_URL


class LoginPage(BasePage):

    URL = BASE_URL

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
