from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://seleniumbase.io/demo_page')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
lnk=driver.find_elements(By.TAG_NAME,'a')
###print all links visible text
for links in lnk:
    print("links text is:",links.text)
    print("link value is",links.get_attribute('href'))
    print()
