# scraper/browser.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Adjust paths if your chrome/chromedriver live elsewhere
    chrome_binary = os.path.abspath("./static_browser/chrome")
    chromedriver_binary = os.path.abspath("./static_browser/chromedriver")

    chrome_options = Options()
    chrome_options.binary_location = chrome_binary
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=chromedriver_binary)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
