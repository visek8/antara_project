from task_2.Page.BasePage import BasePage


# import allure


class MoviePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.MOVIE_NAME = '//*[@class="text el_1"]'
        self.COUNTRY = '//*[@class="text el_5 __countrySB__"]'
        self.SEARCH = '//*[@class="el_18 submit nice_button"]'
        self.POTTER = "Гарри Поттер"
        self.POSTER_POTTER = '//*[@class="element most_wanted"]'
        self.USA = 'США'
        self.ANIME = 'аниме'
        self.CEREMONY = 'церемония'
        self.BIOGRAPHY = 'биография'
        self.JAPAN = 'Япония'
        self.AOT = 'Атака титанов'
        self.OSKAR = 'оскар'
        self.OSKAR_POSTER = '//*[@id="block_left_pad"]/div/div[3]/div[2]'
        self.RUSSIA = 'Россия'
        self.PUSHKIN = '//*[@id="block_left_pad"]/div/div[3]/div[5]'
        self.SVATY = 'сваты'
        self.COMEDY = 'комедия'
        self.SVATY_POSTER = '//*[@class="element most_wanted"]'

    def search_potter(self):
        self.fill_field(self.MOVIE_NAME, self.POTTER)

    def search_svaty(self):
        self.fill_field(self.MOVIE_NAME, self.SVATY)

    def click_on_button(self):
        self.click(self.SEARCH)

    def potter_is_visible(self):
        self.assert_that_element_is_displayed(self.POSTER_POTTER)

    def click_on_country(self):
        self.click(self.COUNTRY)

    def select_usa(self):
        self.click_text(self.USA)

    def select_japan(self):
        self.click_text(self.JAPAN)

    def select_russia(self):
        self.click_text(self.RUSSIA)

    def select_anime(self):
        self.click_text(self.ANIME)

    def select_ceremony(self):
        self.click_text(self.CEREMONY)

    def select_biography(self):
        self.click_text(self.BIOGRAPHY)

    def select_comedy(self):
        self.click_text(self.COMEDY)

    def aot_displayed(self):
        self.assert_that_text_is_displayed(self.AOT)

    def scroll_to_aot(self):
        self.scroll_to_text(self.AOT)

    def scroll_to_potter(self):
        self.scroll(self.POSTER_POTTER)

    def scroll_to_oskar(self):
        self.scroll(self.OSKAR_POSTER)

    def scroll_to_pushkin(self):
        self.scroll(self.PUSHKIN)

    def scroll_to_svaty(self):
        self.scroll(self.SVATY_POSTER)

    def search_oskar(self):
        self.fill_field(self.MOVIE_NAME, self.OSKAR)

    def oskar_is_visible(self):
        self.assert_that_element_is_displayed(self.OSKAR_POSTER)

    def pushkin_is_visible(self):
        self.assert_that_element_is_displayed(self.PUSHKIN)

    def svaty_is_visible(self):
        self.assert_that_element_is_displayed(self.SVATY_POSTER)
