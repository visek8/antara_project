import allure
from task_2.Page.MoviePage import MoviePage


def test_potter(browser_chrome, open_page):
    """In this test we checked whether the Harry Potter
    movie poster will appear when you enter the title"""
    element = MoviePage(browser_chrome)

    with allure.step('Enter Harry Potter into the search bar'):
        element.search_potter()
    with allure.step('Click on the search button'):
        element.click_on_button()
    with allure.step('Scroll to Harry Potter'):
        element.scroll_to_potter()
    with allure.step('We check that the search result includes the film Harry Potter'):
        element.potter_is_visible()


def test_anime_japan(browser_chrome, open_page):
    """In this test we checked whether the Attack on Titan
    poster would appear when selecting a genre and country"""
    element = MoviePage(browser_chrome)

    with allure.step('Choosing an anime genre'):
        element.select_anime()
    with allure.step('Click on the list of countries'):
        element.click_on_country()
    with allure.step('In the drop-down list, select I understand'):
        element.select_japan()
    with allure.step('Click on the search button'):
        element.click_on_button()
    with allure.step('Scroll to anime Attack on Titan'):
        element.scroll_to_aot()
    with allure.step('Checking to see if the search results include the anime Attack on Titan'):
        element.aot_displayed()


def test_ceremony(browser_chrome, open_page):
    """In this test we checked whether the oscar ceremony poster will appear when you enter part of the title,
    select the country and genre"""
    element = MoviePage(browser_chrome)

    with allure.step('Choosing a ceremony genre'):
        element.select_ceremony()
    with allure.step('Click on the list of countries'):
        element.click_on_country()
    with allure.step('Select USA from the drop-down list'):
        element.select_usa()
    with allure.step('Click on the search button'):
        element.click_on_button()
    with allure.step('Scroll to ceremony Oskar'):
        element.scroll_to_oskar()
    with allure.step('We check the Oscar ceremony appeared as a result of the search'):
        element.oskar_is_visible()


def test_biography(browser_chrome, open_page):
    """In this test we checked whether Pushkin's biography
     would appear when choosing a country and genre"""
    element = MoviePage(browser_chrome)

    with allure.step('Click on the list of countries'):
        element.click_on_country()
    with allure.step('Select Russia from the drop-down list'):
        element.select_russia()
    with allure.step('Choosing a biography genre'):
        element.select_biography()
    with allure.step('Click on the search button'):
        element.click_on_button()
    with allure.step('Scroll to biography about Pushkin'):
        element.scroll_to_pushkin()
    with allure.step('we checked whether Pushkin biography would appear'):
        element.pushkin_is_visible()


def test_comedy(browser_chrome, open_page):
    """in this test we checked whether the series matchmakers will appear when you
    enter the name and select the genre"""
    element = MoviePage(browser_chrome)

    with allure.step('Enter сваты in the search bar'):
        element.search_svaty()
    with allure.step('Choosing a comedy genre'):
        element.select_comedy()
    with allure.step('Click on the search button'):
        element.click_on_button()
    with allure.step('Scroll to Matchmakers'):
        element.scroll_to_svaty()
    with allure.step('Checking for the presence of the TV series Matchmakers in the search results'):
        element.svaty_is_visible()
