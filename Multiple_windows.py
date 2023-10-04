from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
print(driver.title)

time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/a').click()

time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])

time.sleep(3)
text=driver.find_element(By.XPATH,'/html/body/div/h3').get_attribute("innerHTML")
print(text)


