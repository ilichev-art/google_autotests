from entities.pages.google_page import GooglePage


def test_google_search(driver):
    page = GooglePage(driver)

    page.open_site() \
        .search('Selenium')
    assert "Selenium" in page.title(), "Результаты поиска не соответствуют запросу"
