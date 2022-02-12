import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("/home/soverton/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("https://defillama.com/protocols/dexes/Polygon")

# Sleep
time.sleep(5)

# Get number of rows in table
rows = 1+len(browser.find_elements_by_xpath(
    "/html/body/div/div/div/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]"))
  
# Get number of columns in table
cols = len(browser.find_elements_by_xpath(
    "/html/body/div/div/div/div[2]/div/div/div[3]/div/div[3]/div/div/div[1]/div[1]/div[3]"))

# Print rows and columns
print("Rows: " + str(rows))
print("Columns: " + str(cols))

browser.quit()
