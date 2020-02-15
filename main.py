#  Aaron Jack tutorial  -- using webdriver.Chrome()
from selenium import webdriver
from time import sleep
from secrets import instaPassword, instaUserName, instaEmail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Instabot:
    def __init__(self, username, pw):
        # self.driver = webdriver.Edge()
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)

        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(instaUserName)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(instaPassword)
        self.driver.find_element_by_xpath(
            '//button[@type="submit"]').click()
        currentUrl = self.driver.current_url
        # print(currentUrl)
        print("after click")
        sleep(4)
        #self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

        sleep(3)
        print("after not now")
# <button class="aOOlW   HoLwm " tabindex="0">Not Now</button>
# /html/body/div[4]/div/div/div[3]/button[2]



Instabot(instaUserName, instaPassword)

if __name__ == "__main__":
    # print("hello")
    pass
