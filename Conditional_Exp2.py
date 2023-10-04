from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://seleniumbase.io/demo_page')
print("radio button 1 is selected or not?",driver.find_element(By.ID,'radioButton1').is_selected())

print("radio button 2 is selected or not?",driver.find_element(By.ID,'radioButton2').is_selected())
time.sleep(3)
driver.switch_to.frame('myFrame3')
driver.find_element(By.ID,'checkBox6').click()
chk=driver.find_element(By.ID,'checkBox6').is_selected()
print("status of checkbox 6",chk)
time.sleep(3)
