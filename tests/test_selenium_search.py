from entities.pages.google_page import GooglePage


def test_google_search(driver):
    page = GooglePage()
    page.open_site() \
        .assert_loaded() \
        .search("Selenium")
    assert "Selenium" in page.title()
