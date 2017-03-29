#encoding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/")

ele = driver.find_element_by_name("W_input")
ele.send_keys("second by se")

ele1 =  driver.find_element_by_class_name('W_btn_a')
ele1.click()