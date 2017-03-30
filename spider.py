#encoding:utf-8
# 开始正式爬虫设计
from selenium import webdriver
# import action chains
from selenium.webdriver.common.action_chains import ActionChains
# import keys
from selenium.webdriver.common.keys import Keys 
# import time
import time
# import file operator
from operator import *
# random
import random

driver = webdriver.Chrome()

# 收集页面中的链接
def gatherLink():
	opened = False
	print("current title"+driver.title)
	links = driver.find_elements_by_css_selector("a")
	print('new page loading')
	for link in links:
		allLink.append(link.get_attribute('href'))
		writeToFile(link.get_attribute('href'))
	print('finish one page -- writen '+str(len(links))+ ' link')
	randomJump()

# 写入文件
def writeToFile(link):
	link = str(link)
	f = open('links.txt','a')
	f.write(link)
	f.write("\n")
	f.close()

# 随便选一个连接，跳转到下一页
def randomJump():
	num = int(random.random()*(len(allLink)-1))
	strLink = allLink[num]
	if(strLink[0:4] != "http"):
		randomJump()
	driver.get(strLink)

	driver.implicitly_wait(20)
	gatherLink()


allLink = []
# 从百度第一个词开始
start = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=QQ&oq=%25E5%25BE%25AE%25E4%25BF%25A1&rsv_pq=b28a74310002352c&rsv_t=9a25FAe5iI0oBtkJggbiH%2FYYm4DC6yQnyLiEy5xc6EDJXlZW91NkF3HNWaA&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&inputT=970&rsv_sug4=1607"

driver.get(start)
# driver.set_window_size(180,200)
gatherLink()
# inputBar = driver.find_element_by_css_selector("#kw")
# inputBar.clear()
# time.sleep(1)
# inputBar.send_keys(Keys.CONTROL,"v")
# inputBar.send_keys(Keys.ENTER)
# time.sleep(2)
# gatherLink()

