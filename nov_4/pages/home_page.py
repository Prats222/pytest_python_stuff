from selenium.webdriver.common.by import By
from .base_page import BasePage
from .article_page import ArticlePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")

    def load(self):
        self.open("/wiki/Main_Page")

    def search(self, query: str) -> ArticlePage:
        # Type then submit with ENTER (avoids banners overlaying the button)
        self.type(self.SEARCH_INPUT, query)
        self.press_enter(self.SEARCH_INPUT)
        return ArticlePage(self.driver)

    def go_to_random(self) -> ArticlePage:
        # Open Random directly
        self.open("/wiki/Special:Random")
        return ArticlePage(self.driver)
