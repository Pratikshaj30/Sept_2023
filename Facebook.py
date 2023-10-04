import time

from selenium import webdriver
driver =webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.amazone.com")
print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.back()
time.sleep(5)
driver.forward()
driver.close()





