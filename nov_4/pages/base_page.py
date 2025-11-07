from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = "https://en.wikipedia.org"
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, path: str = "/"):
        self.driver.get(f"{self.BASE_URL}{path}")

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator, text: str, clear_first: bool = True):
        el = self.find_visible(locator)
        if clear_first:
            el.clear()
        el.send_keys(text)

    def press_enter(self, locator):
        el = self.find_visible(locator)
        el.send_keys(Keys.ENTER)

    def text_of(self, locator) -> str:
        return self.find_visible(locator).text
