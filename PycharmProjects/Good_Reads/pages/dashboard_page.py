from playwright.sync_api import Page

def logo_visible(page):
    logo = page.get_by_role("link", name="Goodreads: Book reviews, recommendations, and discussion")
    return logo