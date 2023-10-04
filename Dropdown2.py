import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://seleniumbase.io/demo_page')
driver.maximize_window()
print(driver.title)

dropdown_list=driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[7]/td[2]/select')

s=Select(dropdown_list)
s.select_by_visible_text('Set to 100%')
time.sleep(3)
s.select_by_index(1)
time.sleep(3)
s.select_by_value('75%')
time.sleep(3)
for option in s.options:
    print(option.text)
    print(option.get_attribute('value'))
driver.close()








