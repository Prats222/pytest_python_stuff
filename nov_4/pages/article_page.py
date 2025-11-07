from selenium.webdriver.common.by import By
from .base_page import BasePage

class ArticlePage(BasePage):
    HEADING = (By.ID, "firstHeading")

    def heading_text(self) -> str:
        return self.text_of(self.HEADING)

    def is_loaded(self) -> bool:
        try:
            text = self.heading_text()
            return bool(text and text.strip())
        except Exception:
            return False
