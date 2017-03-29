#encoding:utf-8
from selenium import webdriver
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

ele = driver.find_element_by_id("kw")
ele.send_keys("some text")

ele1 =  driver.find_element_by_id('su')
ele1.click()