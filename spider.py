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
start = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%95%B0%E6%8D%AE%E5%BA%93&oq=%25E4%25B8%2596%25E7%2595%258C%25E5%258D%2581%25E5%25A4%25A7%25E9%25BB%2591%25E5%25AE%25A2&rsv_pq=81d810110001fc85&rsv_t=0dc0TLK5%2FGWiLLaM7UL9qN2pgk9JpJujCjpxoxCVXQ1JrVfE5c%2B76X1wVgg&rqlang=cn&rsv_enter=1&rsv_sug3=16&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&inputT=3445&rsv_sug4=29538"

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

