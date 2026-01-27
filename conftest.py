import pytest
from playwright.sync_api import sync_playwright
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
