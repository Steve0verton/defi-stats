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
browser.get("https://defillama.com/protocols/dexes/Ethereum")

# Sleep
time.sleep(3)

# Load entire page through infinite scroll by triggering JS
# TODO: current_last_elem CSS selector path seems very distinct and randomly generated, figure out how to make more dynamic and universal
# NOTE: Ensure the "last-child" CSS selector function is used to dynamically find the end
last_elem = ''
while True:
    current_last_elem = "#center > div > div > div.Panel-sc-oefbp0-0.jqKcsO.css-vurnku > div > div.TokenList__List-sc-1a76325-0.JVran.css-1yh09yi > div > div > div:last-child"
    scroll = "document.querySelector(\'" + current_last_elem + "\').scrollIntoView();"
    browser.execute_script(scroll) # execute the js scroll
    print("Last Element= " + last_elem)
    print("Current Element=" + current_last_elem)
    time.sleep(3) # wait for page to load new content
    if (last_elem == current_last_elem):
       break
    else:
       last_elem = current_last_elem 

# Debug output
# with open('output.html', 'w') as f:
#     f.write(browser.page_source)

# Get number of rows in table
rows = len(browser.find_elements(By.XPATH,
    "/html/body/div/div/div/div[2]/div/div/div[3]/div/div[3]/div/div/div"))
  
# Print rows 
print("Rows to scrape: " + str(rows))

# for r in range(2, rows+1):
#     for p in range(1, 6):
#         value = driver.find_element_by_xpath(
#             "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
#         print(value, end='       ')
#     print()

browser.quit()
