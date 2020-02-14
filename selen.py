# selen.py - Advanced Python Programming: Browser Automation with Selenium
# Search Selenium   seleniumhq.org/download
# select a driver
# Uses EDGE

from selenium import webdriver
from time import sleep

driver = webdriver.Edge(
    "C:\\Users\\alanw\\AppData\\Local\\Programs\\Python\\Python38\\MicrosoftWebDriver.exe")
driver.get("https://instagram.com")

sleep(2)
