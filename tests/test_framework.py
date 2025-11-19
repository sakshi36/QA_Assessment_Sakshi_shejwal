import json
import re
import pytest
from playwright.sync_api import Playwright, expect

# Load test data
with open("data/credentials.json") as f:
    user_list = json.load(f)["user_credentials"]


@pytest.mark.order(1)
@pytest.mark.parametrize(
    "user_cred",
    [cred for cred in user_list if cred["username"] != "locked_out_user"]
)
def test_happy_path_clean(playwright: Playwright, user_cred):
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context(record_video_dir="videos1/")
    page = context.new_page()

    try:
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", user_cred["username"])
        page.fill("#password", user_cred["password"])
        page.get_by_role("button", name="Login").click()

        # Wait / assert inventory loaded
        expect(page.locator(".title")).to_have_text("Products", timeout=5000)

        # Add product to cart (first visible add-to-cart)
        page.click("button[id^='add-to-cart']")
        expect(page.locator(".shopping_cart_badge")).to_have_text("1", timeout=3000)

        # Go to cart and checkout
        page.click(".shopping_cart_link")
        page.click("#checkout")

        # Fill details and continue
        page.fill("#first-name", "Test")
        page.fill("#last-name", "User")
        page.fill("#postal-code", "12345")
        page.get_by_role("button", name="Continue").click()

        # Wait for summary to appear
        # expect(page.locator(".summary_info_label")).to_be_visible(timeout=5000)

        # Finish and assert success with case-insensitive match
        page.click("#finish")
        expect(page.locator(".complete-header")).to_have_text(
            re.compile(r"thank you for your order", re.I), timeout=5000
        )
    finally:
        # always cleanup
        context.close()
        browser.close()


@pytest.mark.order(2)
@pytest.mark.parametrize(
    "user_cred",
    [cred for cred in user_list if cred["username"] == "locked_out_user"]
)
def test_locked_out_clean(playwright: Playwright, user_cred):
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context(record_video_dir="videos2/")
    page = context.new_page()

    try:
        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", user_cred["username"])
        page.fill("#password", user_cred["password"])
        page.click("#login-button")

        error = page.locator("div.error-message-container.error")
        expect(error).to_be_visible(timeout=5000)
        expect(error).to_have_text(
            re.compile(r"sorry, this user has been locked out", re.I), timeout=3000
        )
    finally:
        context.close()
        browser.close()
