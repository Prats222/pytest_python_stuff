from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_driver():
    d = webdriver.Chrome()
    d.maximize_window()
    try:
        d.execute_script("document.querySelector('#fixedban')?.remove();")
        d.execute_script("document.querySelectorAll('iframe').forEach(a => a.remove());")
    except Exception:
        pass
    return d

def alerts_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        js_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        driver.execute_script("arguments[0].click();", js_alert)
        time.sleep(0.5)
        a = driver.switch_to.alert
        print("JS Alert text:", a.text)
        a.accept()
        time.sleep(0.5)

        js_confirm = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        driver.execute_script("arguments[0].click();", js_confirm)
        time.sleep(0.5)
        a = driver.switch_to.alert
        print("JS Confirm text:", a.text)
        a.dismiss()
        time.sleep(0.5)

        js_prompt = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        driver.execute_script("arguments[0].click();", js_prompt)
        time.sleep(0.5)
        a = driver.switch_to.alert
        a.send_keys("Selenium Demo")
        a.accept()
        time.sleep(0.5)
        result = driver.find_element(By.ID, "result").text
        print("Prompt result:", result)
    finally:
        driver.quit()

def right_click_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/context_menu")
        box = driver.find_element(By.ID, "hot-spot")
        actions = ActionChains(driver)
        actions.context_click(box).perform()
        time.sleep(0.5)
        a = driver.switch_to.alert
        print("Context menu alert text:", a.text)
        a.accept()
        time.sleep(0.5)
    finally:
        driver.quit()

def hover_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/hovers")
        avatars = driver.find_elements(By.CSS_SELECTOR, ".figure")
        for i, av in enumerate(avatars[:3], start=1):
            actions = ActionChains(driver)
            actions.move_to_element(av).perform()
            time.sleep(0.7)
            caption = av.find_element(By.CSS_SELECTOR, ".figcaption h5").text
            print(f"Hover {i} caption:", caption)
        time.sleep(0.5)
    finally:
        driver.quit()

def windows_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/windows")
        parent = driver.current_window_handle
        link = driver.find_element(By.LINK_TEXT, "Click Here")
        driver.execute_script("arguments[0].click();", link)
        time.sleep(1)
        handles = driver.window_handles
        print("Total windows opened:", len(handles))
        for h in handles:
            if h == parent:
                continue
            if h not in driver.window_handles:
                continue
            driver.switch_to.window(h)
            time.sleep(0.5)
            title = driver.title
            body = ""
            try:
                body = driver.find_element(By.TAG_NAME, "body").text
            except Exception:
                pass
            print("Window:", driver.current_window_handle, "Title:", title, "Body snippet:", (body[:80] if body else "<no body>"))
            if h in driver.window_handles:
                driver.close()
            time.sleep(0.5)
        if parent in driver.window_handles:
            driver.switch_to.window(parent)
            print("Back to parent title:", driver.title)
    finally:
        driver.quit()

def drag_drop_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")
        actions = ActionChains(driver)
        try:
            actions.drag_and_drop(source, target).perform()
            time.sleep(1)
            col_a = driver.find_element(By.ID, "column-a").text
            col_b = driver.find_element(By.ID, "column-b").text
            print("After drag_and_drop - A:", col_a, "B:", col_b)
        except Exception:
            js = """
            function simulateDragDrop(source, target) {
              var dataTransfer = new DataTransfer();
              source.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dataTransfer, bubbles:true, cancelable:true}));
              target.dispatchEvent(new DragEvent('drop', {dataTransfer: dataTransfer, bubbles:true, cancelable:true}));
              source.dispatchEvent(new DragEvent('dragend', {dataTransfer: dataTransfer, bubbles:true, cancelable:true}));
            }
            simulateDragDrop(arguments[0], arguments[1]);
            """
            driver.execute_script(js, source, target)
            time.sleep(1)
            col_a = driver.find_element(By.ID, "column-a").text
            col_b = driver.find_element(By.ID, "column-b").text
            print("After JS drag - A:", col_a, "B:", col_b)
    finally:
        driver.quit()

def waits_demo():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        start = driver.find_element(By.CSS_SELECTOR, "#start button")
        driver.execute_script("arguments[0].click();", start)
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
        print("Loaded text:", el.text)
    finally:
        driver.quit()

if __name__ == "__main__":
    alerts_demo()
    time.sleep(1)
    right_click_demo()
    time.sleep(1)
    hover_demo()
    time.sleep(1)
    windows_demo()
    time.sleep(1)
    drag_drop_demo()
    time.sleep(1)
    waits_demo()
