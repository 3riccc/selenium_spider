#encoding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.shadowcreator.com/login/login.html")

ele = driver.find_element_by_name("phone")
ele.send_keys("some text")

ele1 =  driver.find_element_by_class_name('loginFunBtn')
ele1.click()