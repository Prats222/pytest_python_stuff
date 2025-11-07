from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Step 1: Open browser and page
driver = webdriver.Chrome()   # make sure chromedriver is in PATH
driver.maximize_window()
driver.get("https://qaplayground.dev/apps/mouse-hover/")
time.sleep(2)  # wait for page to load fully

# Step 2: Find all the hoverable boxes
boxes = driver.find_elements(By.CLASS_NAME, "card")
print("Found", len(boxes), "hover boxes.\n")

# Step 3: Create ActionChains
actions = ActionChains(driver)

# Step 4: Loop through each box and test hover
for i, box in enumerate(boxes, start=1):
    before = box.value_of_css_property("background-color")
    print(f"Box {i} -> Before hover color:", before)

    # Hover over box
    actions.move_to_element(box).perform()
    time.sleep(1)

    after = box.value_of_css_property("background-color")
    print(f"Box {i} -> After hover color: ", after)
    print("-" * 40)

# Step 5: Keep page open for 10 seconds so you can see the effect
print("✅ Hover test finished! Check your browser window — boxes changed color.")
time.sleep(10)

driver.quit()
