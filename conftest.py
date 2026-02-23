import os
import shutil
import pytest
import allure
from datetime import datetime
from playwright.sync_api import sync_playwright
from settings import STANDARD_USER, PASSWORD, HEADLESS
from pages.login_page import LoginPage


# ---------------------------
# Clean old artifacts
# ---------------------------

ARTIFACT_DIRS = ["screenshots", "videos", "traces", "state"]

def clean_artifacts():
    for folder in ARTIFACT_DIRS:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)


@pytest.fixture(scope="session", autouse=True)
def cleanup_before_run():
    clean_artifacts()


# ---------------------------
# Playwright / Browser setup
# ---------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser to run tests: chromium, firefox, webkit"
    )


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, request):
    browser_name = request.config.getoption("--browser_name")

    browser_type = getattr(playwright_instance, browser_name)

    browser = browser_type.launch(headless=HEADLESS)
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
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    storage_path = "state/auth.json"
    context.storage_state(path=storage_path)
    context.close()

    return storage_path


# ---------------------------
# Context per test
# ---------------------------

@pytest.fixture
def context(browser, auth_storage, request):
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    video_dir = os.path.join("videos", test_name)
    os.makedirs(video_dir, exist_ok=True)

    context = browser.new_context(
        storage_state=auth_storage,
        record_video_dir=video_dir
    )

    trace_path = os.path.join("traces", f"{test_name}_{timestamp}.zip")

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.tracing.stop(path=trace_path)
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ---------------------------
# Screenshot + Allure attachment on failure
# ---------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        page = item.funcargs.get("page")

        if page and result.failed:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            trace_file = next(
                (f for f in os.listdir("traces") if item.name in f),
                None
            )

            if trace_file:
                allure.attach.file(
                    f"traces/{trace_file}",
                    name="Trace",
                    attachment_type=allure.attachment_type.ZIP
                )
