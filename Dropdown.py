from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://seleniumbase.io/demo_page')
print(driver.title)
print(driver.current_url)
# dropdown1=driver.find_element(By.ID,'mySelect')
# time.sleep(3)
# S=Select(dropdown1)
# S.select_by_visible_text('Set to 75%')
# time.sleep(3)
# S.select_by_value('100%')
# time.sleep(3)
# S.select_by_index(1)
# time.sleep(3)
# S.select_by_visible_text('Set to 25%')
# print(len(S.options))
### Print all options visible text,all value and index

DropdownList = driver.find_element(By.ID, 'mySelect')
dropdown=Select(DropdownList)
for option in dropdown.options:
    print("the text is",option.text+"the value is",option.get_attribute('value'))


