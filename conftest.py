import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from settings import HEADLESS, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# ----------------------------
# Browser setup
# ----------------------------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "firefox":
        browser = playwright_instance.firefox.launch(headless=HEADLESS)
    elif browser_name == "webkit":
        browser = playwright_instance.webkit.launch(headless=HEADLESS)
    else:
        browser = playwright_instance.chromium.launch(headless=HEADLESS)

    yield browser
    browser.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser: chromium | firefox | webkit",
    )


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ----------------------------
# Business fixtures
# ----------------------------

@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login(STANDARD_USER, PASSWORD)
    return page


@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)


@pytest.fixture
def cart_with_item(inventory_page):
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()


# ----------------------------
# Allure attachments on failure
# ----------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            # Screenshot
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            # Trace file (if enabled)
            trace_path = os.path.join("trace.zip")
            try:
                page.context.tracing.stop(path=trace_path)
                if os.path.exists(trace_path):
                    with open(trace_path, "rb") as f:
                        allure.attach(
                            f.read(),
                            name="trace",
                            attachment_type=allure.attachment_type.ZIP,
                        )
                    os.remove(trace_path)
            except Exception:
                pass
