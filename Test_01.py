# coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Edge("./edge/msedgedriver.exe")

driver.maximize_window()
print("浏览器最大化")

url='http://172.16.75.120:8080/NetShark/#/login'

url_baidu='https://www.baidu.com/'

driver.get(url)
print("now access %s" %(url))
time.sleep(2)

driver.get(url_baidu)
print("now access %s" %(url_baidu))
time.sleep(2)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)


driver.set_window_size(600,800)

time.sleep(10)
driver.close()