import pytest
from playwright.sync_api import Playwright
from utils import data_handle

@pytest.fixture
def launch_website(playwright:Playwright,page):
    config_path="config.dev.json"
    dev_url = data_handle.get_json_data("dev_url",config_path)
    browser = data_handle.get_json_data("browser", config_path)
    page.goto(dev_url)
    yield page
    page.context.close()