from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/ul/li[1]/button').click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(3)

driver.close()




