# Lab 5 - Screenshot & Broken Link

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# open browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)

    # take screenshot
    driver.save_screenshot("practice_page.png")
    print("Screenshot saved.")

    # find broken link
    link = driver.find_element(By.LINK_TEXT, "Broken Link")
    url = link.get_attribute("href")

    # check status
    res = requests.get(url)
    code = res.status_code

    if code >= 404:
        print("The link is broken!")
    else:
        print("The link is valid.")

    time.sleep(2)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
