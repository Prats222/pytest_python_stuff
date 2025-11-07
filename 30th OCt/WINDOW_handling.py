from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def multiple_windows_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demoqa.com/browser-windows")

        parent_window = driver.current_window_handle

        # Open multiple windows
        driver.find_element(By.ID, "windowButton").click()
        time.sleep(1)
        driver.find_element(By.ID, "messageWindowButton").click()
        time.sleep(1)

        # Get all windows
        all_windows = driver.window_handles
        print(f"Total windows opened: {len(all_windows)}")

        # Switch to and close each window except parent
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print(f"Window: {driver.current_window_handle}")
                print(f"Title: {driver.title}")
                driver.close()
                time.sleep(1)

        # Switch back to parent
        driver.switch_to.window(parent_window)
        print(f"Final window: {driver.title}")

    finally:
        driver.quit()


multiple_windows_demo()
