import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
time.sleep(3)
inputdropdown = driver.find_element(By.ID,'dropOption1')

print(inputdropdown.is_displayed())
print(driver.find_element(By.ID,'myTextInput2').is_displayed())
print('radio button1 selected or not: ',driver.find_element(By.ID,'radioButton1').is_selected())
print('radio button2 selected or not: ',driver.find_element(By.ID,'radioButton2').is_selected())

##check if read only or not


print("Attribute is : ",driver.find_element(By.ID,'myTextInput2').get_attribute('readonly'))

##click on the radio button
driver.find_element(By.ID,'radioButton2').click()
time.sleep(5)
status=driver.find_element(By.ID,'radioButton2').is_selected()
print('radio button 2 is selected or not :', status)

