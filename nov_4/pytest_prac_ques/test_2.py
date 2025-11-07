import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def slow(s=1.0):
    time.sleep(s)

def test_string_operations_on_selenium_dev():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://www.selenium.dev/")
        slow(1.5)

        title = driver.title
        print(f"\nPage Title: {title}")

        body_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"Page text length: {len(body_text)}")
        print(f"First 150 chars of page text:\n{body_text[:150]}...\n")

        assert "Selenium" in title
        assert "browser automation" in body_text.lower() or "selenium" in body_text.lower()
        assert 5 < len(title) < 100
        assert len(body_text) > 500
        assert "Selenium" in title
        assert "selenium" != title
        assert title.strip().startswith("Selenium")
        assert not title.islower()
        assert title.split()[0] == "Selenium"

        print("✅ All string assertions passed successfully!\n")
        slow(1)
    finally:
        driver.quit()
