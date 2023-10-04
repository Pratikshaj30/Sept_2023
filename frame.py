from selenium import webdriver

import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
driver.maximize_window()
print(driver.title)
driver.switch_to.frame('iframeResult')
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/button').click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.close()
