from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


def navigation_commands():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        # Using get() method
        driver.get("https://www.google.com")
        print(f"Page 1: {driver.title}")
        time.sleep(2)

        # Using navigate().to() method
        driver.get("https://www.facebook.com")
        print(f"Page 2: {driver.title}")
        time.sleep(2)

        # Navigate back
        driver.back()
        print(f"After back: {driver.title}")
        time.sleep(2)

        # Navigate forward
        driver.forward()
        print(f"After forward: {driver.title}")
        time.sleep(2)

        # Refresh page
        driver.refresh()
        print("Page refreshed")

    finally:
        driver.quit()


navigation_commands()

