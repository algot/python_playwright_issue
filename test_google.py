from playwright.sync_api import Page

from env_config import EnvConfig


class TestGoogle:
    def test_google_title(self, page: Page, env_config: EnvConfig):
        page.goto(env_config.url)
        assert page.title() == 'Google'
