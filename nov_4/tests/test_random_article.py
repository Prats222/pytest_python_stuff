import pytest
import os, sys
# from .../nov_4/tests -> go two levels up to project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from nov_4.pages.home_page import HomePage
 # adds .../nov_4 to sys.path

import time
from selenium import webdriver
from nov_4.pages.home_page import HomePage



def test_random_article_has_heading():

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:
        home = HomePage(driver)
        home.load()
        article = home.go_to_random()
        assert article.is_loaded() is True
        assert len(article.heading_text().strip()) > 0
    finally:
        time.sleep(2)
        driver.quit()
