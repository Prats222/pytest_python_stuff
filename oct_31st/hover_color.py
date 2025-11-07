from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://ianlunn.github.io/Hover/")
    time.sleep(3)

    element = driver.find_element(By.XPATH, '//*[@id="effects"]/a[30]')

    # into view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)

    actions = ActionChains(driver)

    # color before hover
    color_before = element.value_of_css_property("background-color")
    print("Before hover color:", color_before)

    # Hover
    actions.move_to_element(element).perform()
    time.sleep(1)

    # color after hover
    color_after = element.value_of_css_property("background-color")
    print("After hover color :", color_after)

finally:
    driver.quit()
