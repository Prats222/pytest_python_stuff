# Lab 3 - Dropdowns (Select Class)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# open browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get("https://demo.automationtesting.in/Register.html")
    #time.sleep(2)

    # scroll down
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)

    # skill
    skill = Select(driver.find_element(By.XPATH, "//*[@id='Skills']"))
    skill.select_by_visible_text("Adobe Photoshop")



    # select country (custom dropdown)
    country_dropdown = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[10]/div/span/span[1]/span")
    driver.execute_script("arguments[0].scrollIntoView();", country_dropdown)
    country_dropdown.click()
    time.sleep(2)

    # type and select Japan
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.send_keys("Japan")
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)
    # year
    year = Select(driver.find_element(By.XPATH, "//*[@id='yearbox']"))
    year.select_by_index(5)

    # languages
    lang = driver.find_element(By.XPATH, "//*[@id='msdd']")
    lang.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='English']").click()
    driver.find_element(By.XPATH, "//a[text()='French']").click()

    time.sleep(2)

except Exception as e:
    print("Error:", e)

# close browser
finally:
    driver.quit()
