import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title)
print(driver.current_url)
time.sleep(5)
inputele=driver.find_element(By.NAME,'username')
inputele.send_keys("Admin")

inputpass=driver.find_element(By.NAME,'password')
inputpass.send_keys("admin123")

btnlogin = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")

btnlogin.click()
time.sleep(5)
driver.close()




