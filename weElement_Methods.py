from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def webelement_methods():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com")

        # Find element
        username = driver.find_element(By.ID, "user-name")

        # 1. send_keys() - Enter text
        username.send_keys("standard_user")

        time.sleep(2)
        # 2. clear() - Clear text
        username.clear()
        username.send_keys("problem_user")

        time.sleep(2)

        username.clear()
        username.send_keys("standard_user")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")

        # 3. click() - Click element
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        time.sleep(2)

        # 4. get_attribute() - Get attribute value
        menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
        class_name = menu_btn.get_attribute("class")
        print(f"Class attribute: {class_name}")

        # 5. text - Get text content
        title = driver.find_element(By.CLASS_NAME, "title")
        print(f"Title text: {title.text}")

        # 6. is_displayed() - Check if element is displayed
        is_displayed = menu_btn.is_displayed()
        print(f"Is displayed: {is_displayed}")

        # 7. is_enabled() - Check if element is enabled
        is_enabled = menu_btn.is_enabled()
        print(f"Is enabled: {is_enabled}")

        # 8. is_selected() - Check if element is selected (for checkboxes/radio)
        menu_btn.click()
        time.sleep(1)

        logout_link = driver.find_element(By.ID, "logout_sidebar_link")
        is_selected = logout_link.is_selected()
        print(f"Is selected: {is_selected}")

        # 9. location - Get element location
        location = menu_btn.location
        print(f"Element location: {location}")

        # 10. size - Get element size
        size = menu_btn.size
        print(f"Element size: {size}")

    finally:
        driver.quit()


webelement_methods()
