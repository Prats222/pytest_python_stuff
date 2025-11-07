# Lab 4 - JavaScriptExecutor for Scrolling

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
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)

    # scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # scroll to top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # find mouse hover button and scroll into view
    mouse_hover = driver.find_element(By.ID, "mousehover")
    driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)
    time.sleep(2)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
