import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
time.sleep(3)
alertbtn = driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(1) > button')
alertbtn.click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)



