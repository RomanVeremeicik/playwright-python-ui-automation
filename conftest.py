import os
import pytest
import allure
from pathlib import Path
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from settings import STANDARD_USER, PASSWORD, HEADLESS


# =========================
# PLAYWRIGHT SESSION SETUP
# =========================

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()


# =========================
# BASIC PAGE FIXTURE
# =========================

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    # start tracing for every test
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page

    context.close()


# =========================
# AUTH STORAGE (SESSION LOGIN)
# =========================

@pytest.fixture(scope="session")
def auth_storage(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    storage_path = "storage_state.json"
    context.storage_state(path=storage_path)

    browser.close()
    return storage_path


@pytest.fixture()
def authorized_page(browser, auth_storage):
    context = browser.new_context(storage_state=auth_storage)
    page = context.new_page()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page

    context.close()


# =========================
# ALLURE FAILURE ATTACHMENTS
# =========================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("authorized_page")

        if page:
            context = page.context

            trace_dir = Path("traces")
            trace_dir.mkdir(exist_ok=True)

            trace_path = trace_dir / f"{item.name}.zip"

            context.tracing.stop(path=str(trace_path))

            # attach trace WITHOUT attachment_type
            with open(trace_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name="trace.zip"
                )

            # screenshot attachment
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot.png",
                attachment_type=allure.attachment_type.PNG
            )
