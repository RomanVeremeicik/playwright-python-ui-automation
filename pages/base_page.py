class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def click(self, locator):
        self.page.locator(locator).click()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
