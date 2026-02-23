import os
import pytest
from playwright.sync_api import sync_playwright
from settings import STANDARD_USER, PASSWORD, HEADLESS
from pages.login_page import LoginPage


# ---------------------------
# Browser (session scope)
# ---------------------------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()


# ---------------------------
# Storage state (login once)
# ---------------------------

@pytest.fixture(scope="session")
def auth_storage(browser):
   
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(STANDARD_USER, PASSWORD)

    os.makedirs("state", exist_ok=True)
    storage_path = "state/auth.json"

    context.storage_state(path=storage_path)
    context.close()

    return storage_path


# ---------------------------
# Test context
# ---------------------------

@pytest.fixture
def context(browser, auth_storage):
    
    os.makedirs("videos", exist_ok=True)

    context = browser.new_context(
        storage_state=auth_storage,
        record_video_dir="videos/"
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ---------------------------
# Screenshot on failure
# ---------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")
