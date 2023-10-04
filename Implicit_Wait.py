from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/button').click()
driver.implicitly_wait(10)
load=driver.find_element(By.XPATH,'//*[@id="loading"]').text

print(load)
text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text

print("Text : ", text)




