# selen.py - Advanced Python Programming: Browser Automation with Selenium
# Search Selenium   seleniumhq.org/download
# select a driver
# Uses EDGE

from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get("https://instagram.com")

sleep(2)
