from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def fluent_wait_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(driver, 15, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

        products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("Products are visible")

        product_item = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
        product_item.click()
        print("Product clicked")

        wait.until(EC.url_contains("inventory-item"))
        print("Navigated to product details")
    finally:
        driver.quit()

fluent_wait_demo()
