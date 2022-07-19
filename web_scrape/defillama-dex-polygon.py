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
webdriver_service = Service("/usr/local/bin/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("https://defillama.com/protocols/dexes/Ethereum")

# Sleep
time.sleep(1)

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Debug output
with open('output.html', 'w') as f:
    f.write(browser.page_source)

# Get number of rows in table
rows = len(browser.find_elements(By.XPATH,
    "/html/body/div[1]/div/main/section/div/div/table/tbody/tr[1]"))

# Print rows 
print("Rows to scrape: " + str(rows))

# Print output to screen
# for r in range(2, rows+1):
#     for p in range(1, 6):
#         value = driver.find_element_by_xpath(
#             "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
#         print(value, end='       ')
#     print()

browser.quit()
