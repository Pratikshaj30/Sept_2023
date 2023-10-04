from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://www.facebook.com/')
print(driver.title)
print(driver.current_url)
usrname=driver.find_element(By.ID,'email')
usrname.send_keys('jpratiksha5000@gmail.com')

passw=driver.find_element(By.ID,'pass')
passw.send_keys('pratiksha@123')

loginbtn=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
time.sleep(3)
driver.close()