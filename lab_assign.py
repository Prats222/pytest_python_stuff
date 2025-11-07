from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def webelement_methods_lab_assign():
    driver = webdriver.Chrome()

    try:
        # website
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1)

        # Findn username input ,entern text
        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        time.sleep(1)

        #  Clearin  text and re-entern
        username.clear()
        username.send_keys("invalid_user")
        time.sleep(1)

        username.clear()
        username.send_keys("tomsmith")

        #  Find password box and enter password
        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")

        #  Click the login button
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Get attribute before clicking
        print("Login button type:", login_btn.get_attribute("type"))

        # Check if displayed and enabled
        print("Is login button displayed:", login_btn.is_displayed())
        print("Is login button enabled:", login_btn.is_enabled())

        login_btn.click()
        time.sleep(2)

        # After login, get page heading text
        heading = driver.find_element(By.TAG_NAME, "h2")
        print("Heading text:", heading.text)

        # flash card pe click
        flash = driver.find_element(By.ID, "flash")
        print("Flash message:", flash.text.split("\n")[0])

        # Movin to checkbox pge
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(2)

        # Find checkboxes
        checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

        print("Checkbox1 initially selected:", checkbox1.is_selected())
        print("Checkbox2 initially selected:", checkbox2.is_selected())

        #  first checkbx
        driver.execute_script("arguments[0].scrollIntoView();", checkbox1)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", checkbox1)
        time.sleep(1)
        print("Checkbox1 selected after click:", checkbox1.is_selected())

        # 2nd checkbx
        print("Checkbox2 location:", checkbox2.location)
        print("Checkbox2 size:", checkbox2.size)

    finally:
        time.sleep(1)
        driver.quit()


webelement_methods_lab_assign()
