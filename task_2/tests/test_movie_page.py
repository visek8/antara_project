# import allure
from task_2.Page.MoviePage import MoviePage


def test_potter(browser_chrome, open_page):
    element = MoviePage(browser_chrome)

    element.search_potter()
    element.click_on_button()
    element.potter_is_visible()


def test_anime_japan(browser_chrome, open_page):
    element = MoviePage(browser_chrome)

    element.select_anime()
    element.click_on_country()
    element.select_japan()
    element.click_on_button()
    element.aot_displayed()


def test_ceremony(browser_chrome, open_page):
    element = MoviePage(browser_chrome)

    element.select_ceremony()
    element.click_on_country()
    element.select_usa()
    element.click_on_button()
    element.oskar_is_visible()


def test_biography(browser_chrome, open_page):
    element = MoviePage(browser_chrome)

    element.click_on_country()
    element.select_russia()
    element.select_biography()
    element.click_on_button()
    element.pushkin_is_visible()


def test_comedy(browser_chrome, open_page):
    element = MoviePage(browser_chrome)

    element.search_svaty()
    element.select_comedy()
    element.click_on_button()
    element.svaty_is_visible()