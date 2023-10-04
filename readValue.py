import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
inputEle=driver.find_element(By.ID,'myTextInput2')
print("ID is:",inputEle.get_attribute('id'))
print("Name is:",inputEle.get_attribute('name'))
print("Value is:",inputEle.get_attribute('value'))
print("Type is:",inputEle.get_attribute('type'))
time.sleep(3)
driver.close()



