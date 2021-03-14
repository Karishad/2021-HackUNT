# Kieron Yin
# 3/13/2021
# For HackUNT
# Purpose: Use selenium to scrape data from Twitter

import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox

driver = Firefox()
driver.get('https://twitter.com/login')

username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('test')
