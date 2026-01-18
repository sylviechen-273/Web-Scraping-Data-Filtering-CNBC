from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time


# the target url
url = "https://www.cnbc.com/world/?region=world"

# set the options for Firefox browser
options = Options()
options.add_argument("-headless")
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

# set the geckodriver
service = Service("/usr/local/bin/geckodriver")

# start the browser and get the html
browser = webdriver.Firefox(service=service, options=options)
browser.get(url)

time.sleep(8)

content = browser.page_source


# save the html into the raw_data folder
with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as file:
    file.write(content) 

# exit the browser
browser.quit()
