# Lab 2 - Radio Buttons & Checkboxes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# open browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get("https://demo.automationtesting.in/Register.html")
    time.sleep(2)

    # select male radio
    male = driver.find_element(By.XPATH, "//input[@value='Male']")
    male.click()
    print("Male selected:", male.is_selected())

    time.sleep(2)
    # select cricket
    cricket = driver.find_element(By.XPATH, "//input[@value='Cricket']")
    cricket.click()

    time.sleep(2)
    # select movies
    movies = driver.find_element(By.XPATH, "//input[@value='Movies']")
    movies.click()
    time.sleep(2)
    # deselect movies
    movies.click()

    # check status
    print("Cricket selected:", cricket.is_selected())
    print("Movies selected:", movies.is_selected())

    time.sleep(2)

except Exception as e:
    print("Error:", e)

# close browser
finally:
    driver.quit()
