import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=option)
driver.get('https://demoqa.com/webtables')

# delete existing data
delButton = len(driver.find_elements(By.XPATH, '//span[@title="Delete"]'))

# # delete existing data
for delete in range(1,delButton+1):
    driver.find_element(By.ID, 'delete-record-'+str(delete)).click()
# driver.find_element(By.ID, 'delete-record-1').click()
# driver.find_element(By.ID, 'delete-record-2').click()
# driver.find_element(By.ID, 'delete-record-3').click()
time.sleep(3)

# new data
staffs = [
        {
            'FirstName': 'Ilham',
            'LastName': 'Apriansyah',
            'Email': 'ilhamapriansyah@gmail.com',
            'Age': 26,
            'Salary': 7000000,
            'Departement' : 'QA'
        },
        {
            'FirstName': 'Tri',
            'LastName': 'Handoko',
            'Email': 'kokotri@gmail.com',
            'Age': 28,
            'Salary': 8000000,
            'Departement' : 'BE'
        },
        {
            'FirstName': 'Bagus',
            'LastName': 'Lazuardi',
            'Email': 'lazuardibagus@gmail.com',
            'Age': 26,
            'Salary': 6000000,
            'Departement' : 'FE'
        }
]


# add new data
for staff in staffs:
    driver.find_element(By.ID, 'addNewRecordButton').click()

    # Explicitly Wait modal
    try:
        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, 'submit')))
    # input data
        driver.find_element(By.ID, 'firstName').send_keys(staff['FirstName'])
        driver.find_element(By.ID, 'lastName').send_keys(staff['LastName'])
        driver.find_element(By.ID, 'userEmail').send_keys(staff['Email'])
        driver.find_element(By.ID, 'age').send_keys(staff[str('Age')])
        driver.find_element(By.ID, 'salary').send_keys(staff[str('Salary')])
        driver.find_element(By.ID, 'department').send_keys(staff['Departement'])
    # submit data
        driver.find_element(By.ID, 'submit').click()

    except TimeoutException:
        print('Modal not shown')
        pass
    
time.sleep(3)

driver.close()









