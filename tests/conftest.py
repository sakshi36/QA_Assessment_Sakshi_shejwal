import os
import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def headed():
    # Control headed vs headless by env var: HEADLESS=0 to see browser
    return os.getenv("HEADLESS", "1") == "0"

@pytest.fixture
def launch_browser(playwright: Playwright, headed):
    browser = playwright.chromium.launch(headless=not headed)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    yield page
    context.close()
    browser.close()

def pytest_exception_interact(node, call, report):
    # This is a simple placeholder; using pytest-playwright you can use their hooks/plugins to capture automatically
    pass