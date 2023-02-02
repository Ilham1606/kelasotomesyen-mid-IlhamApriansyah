from selenium import webdriver
import time

websites = ["https://tiket.com", "https://tokopedia.com", "https://orangsiber.com", "https://demoqa.com", "https://automatetheboringstuff.com"]

for judul in websites:
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(judul)
    print(driver.title)
    time.sleep(2)
    
driver.close()