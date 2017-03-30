#encoding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")
print("width 480 height 800")

# driver.set_window_size(480,800)
driver.maximize.window()
# driver.quit()