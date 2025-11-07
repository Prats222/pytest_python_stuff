import pytest
import os, sys
# from .../nov_4/tests -> go two levels up to project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import time
from selenium import webdriver


from nov_4.pages.home_page import HomePage


def test_search_opens_correct_article():

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:
        home = HomePage(driver)
        home.load()
        article = home.search("Selenium (software)")
        assert article.is_loaded() is True
        assert article.heading_text() == "Selenium (software)"
    finally:
        time.sleep(2)
        driver.quit()
