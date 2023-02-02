from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://google.com')
time.sleep(5)
driver.get('https://twitter.com')
time.sleep(5)