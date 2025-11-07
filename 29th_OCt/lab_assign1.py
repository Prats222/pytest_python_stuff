# Lab 1 - Navigation & WebElement Methods

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
    driver.get("https://demo.automationtesting.in/Index.html")

    # click skip sign in
    driver.find_element(By.ID, "btn2").click()
    time.sleep(3)

    # fill first name
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Prateek")

    # fill last name
    driver.find_element(By.XPATH, "//input[@ng-model='LastName']").send_keys("Mishra")

    # fill address
    try:
        addr = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
    except:
        addr = driver.find_element(By.TAG_NAME, "textarea")
    addr.send_keys("123 Demo Street, New Delhi, India")

    # get header text
    head = driver.find_element(By.TAG_NAME, "h1").text
    print("Header text is:", head)

    # go back
    driver.back()
    time.sleep(2)

except Exception as e:
    print("Error:", e)

# close browser
finally:
    driver.quit()
