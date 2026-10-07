from playwright.sync_api import Page, expect
from pages import dashboard_page as dash_page

def test_home_page_title(launch_website: Page):
    page = launch_website
    expect(page).to_have_title("Goodreads | Meet your next favorite book")

def test_home_page_logo_visible(launch_website: Page):
    page = launch_website
    expect(dash_page.logo_visible()).to_be_visible()


def test_home_page_signup_and_signin_links_visible(launch_website: Page):
    page=launch_website
    expect(page.get_by_role("link", name="continue with Amazon")).to_be_visible()
    expect(page.get_by_role("link", name="continue with apple")).to_be_visible()
    expect(page.get_by_role("link", name="Sign up with email")).to_be_visible()
    expect(page.get_by_role("link", name="Sign in")).to_be_visible()

def test_home_page_search_box_visible(launch_website: Page):
    page = launch_website
    search_box = page.get_by_role("textbox", name="Title / Author / ISBN")
    expect(search_box).to_be_visible()
    expect(search_box).to_be_editable()
    search_box.fill("Harry Potter")
    expect(search_box).to_have_value("Harry Potter")

def test_home_page_genre_links_visible(launch_website: Page):
    page = launch_website
    for genre in ["Art", "Fantasy", "Horror", "Romance", "Thriller"]:
        expect(page.get_by_role("link", name=genre , exact=True)).to_be_visible()

def test_home_page_footer_visible(launch_website: Page):
    page = launch_website
    footer = page.get_by_role("contentinfo")
    expect(footer).to_be_visible()
