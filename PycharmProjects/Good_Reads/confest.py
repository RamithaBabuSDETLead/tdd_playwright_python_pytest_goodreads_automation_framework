import pytest
from playwright.sync_api import Playwright
from setup.browser_config import get_web_app
from utils import data_handle

@pytest.fixture
def launch_website(playwright:Playwright):
    config_path="config.dev.json"
    dev_url = data_handle.get_json_data("dev_url",config_path)
    browser = data_handle.get_json_data("browser", config_path)
    page = get_web_app(browser,dev_url,playwright)
    yield page
    page.context.close()