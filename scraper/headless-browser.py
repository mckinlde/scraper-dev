# scraper/browser.py

import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_binary = shutil.which("chromium")
    chromedriver_binary = shutil.which("chromedriver")

    chrome_options = Options()
    chrome_options.binary_location = chrome_binary
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=chromedriver_binary)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
