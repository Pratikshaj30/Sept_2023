from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
###print all links visible text

links=driver.find_elements(By.TAG_NAME,'a')

for link in links:
    print("visible text is: ",link.text+"and the link is :",link.get_attribute('href'))