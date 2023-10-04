import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
print(driver.title)
print(driver.current_url)
time.sleep(3)
inputElement=driver.find_element(By.NAME,'email')
inputElement.send_keys('jadhav.pratiksha2@gmail.com')
inputpass = driver.find_element(By.NAME,'pass')
inputpass.send_keys('pra@123')
btnlogin = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
btnlogin.click()
time.sleep(3)
driver.close()
driver.quit()






