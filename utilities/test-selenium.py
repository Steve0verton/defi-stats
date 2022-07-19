import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Debug
print("Python System Path=")
print(sys.path)

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("/usr/local/bin/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("https://bitcoin.org")

# Extract description from page and print
description = browser.find_element(By.NAME, "description").get_attribute("content")
print("Meta Description=")
print(f"{description}")

# Wait for 5 seconds
time.sleep(5)
browser.quit()
