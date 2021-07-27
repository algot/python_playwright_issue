import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

from env_config import EnvConfig


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        new_page: Page = browser.new_page()
        new_page.set_viewport_size({'width': 1900, 'height': 1080})

        yield new_page

        browser.close()


@pytest.fixture(scope='session')
def env_config():
    return EnvConfig()
