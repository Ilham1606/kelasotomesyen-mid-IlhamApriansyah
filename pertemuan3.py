import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=option)
driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'promtButton').click()
driver.switch_to.alert.send_keys('Ilham Apriansyah')
driver.switch_to.alert.accept()
time.sleep(3)

driver.close()