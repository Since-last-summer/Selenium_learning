# coding=utf-8


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Edge('./edge/msedgedriver.exe')
driver.get("http://www.baidu.com")
assert "百度" in driver.title
elem=driver.find_element_by_name("wd")
elem.send_keys("seleniumhq"+Keys.RETURN)  #Keys.return 等于 回车 操作

try:
    driver.find_element_by_xpath('//*[@id="kw"]')
except NoSuchElementException:
    assert 0,"can't find seleniumhq"

time.sleep(10)
driver.quit()