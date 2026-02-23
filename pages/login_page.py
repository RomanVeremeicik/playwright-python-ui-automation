from pages.base_page import BasePage
from settings import BASE_URL


class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        super().open(BASE_URL)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
