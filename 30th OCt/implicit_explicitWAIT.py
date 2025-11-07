from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def implicit_wait_demo():
    driver = webdriver.Chrome()

    # Set implicit wait (wait up to 10 seconds for elements)
    driver.implicitly_wait(10)

    try:
        driver.get("https://www.saucedemo.com")

        # These will wait up to 10 seconds if elements are not immediately found
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

    finally:
        driver.quit()


implicit_wait_demo()


def explicit_wait_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com")

        # Login first
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Use explicit wait for specific condition
        wait = WebDriverWait(driver, 10)

        # Wait for products to be visible
        products = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        print("Products are visible")

        # Wait for element to be clickable
        product_item = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        )
        product_item.click()
        print("Product clicked")

        # Wait for URL to contain specific text
        wait.until(EC.url_contains("inventory-item"))
        print("Navigated to product details")

    finally:
        driver.quit()


explicit_wait_demo()
