import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=option)
driver.get('https://demoqa.com/tool-tips')

field = driver.find_element(By. ID, 'toolTipButton')
hidden_field = driver.find_element(By. ID, 'toolTipTextField')

actions = ActionChains(driver)
actions.move_to_element(field)
actions.move_to_element(hidden_field)
actions.click(field)
actions.click(hidden_field)

actions.perform()
time.sleep(3)
