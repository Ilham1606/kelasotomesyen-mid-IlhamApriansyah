from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.maximize_window()
driver.get('https://demoqa.com/text-box')

driver.find_element(By.ID,'userName').send_keys('Ilham')
driver.find_element(By.ID,'userEmail').send_keys('ilhamapriansyah@gmail.com')
driver.find_element(By.ID,'currentAddress').send_keys('Di rumah saya')
driver.find_element(By.ID,'permanentAddress').send_keys('Di Indonesia')
driver.find_element(By.ID,'submit').click()

time.sleep(2)