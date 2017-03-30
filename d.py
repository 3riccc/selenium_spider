#encoding:utf-8
from selenium import webdriver
# import action chains
from selenium.webdriver.common.action_chains import ActionChains
# import keys
from selenium.webdriver.common.keys import Keys 

import time
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")
# while True:
# 	inputBar = driver.find_element_by_css_selector("#kw")
# 	inputBar.clear()
# 	time.sleep(1)
# 	inputBar.send_keys(Keys.CONTROL,"v")
# 	inputBar.send_keys(Keys.ENTER)
# 	time.sleep(1)
# 	driver.refresh()



# 设置尺寸
# print("width 480 height 800")
# driver.set_window_size(480,800)

# 后退
# driver.get("http://you.163.com")
# print("back to baidu")
# driver.back()

# 前进
# print("forward to yanxuan")
# driver.forward()

# 刷新
# print("refresh")
# driver.refresh()

# 写入、清除文本
# inputBar = driver.find_element_by_css_selector("#kw")
# inputBar.clear()
# inputBar.send_keys("kkk")
# time.sleep(2)
# inputBar.clear()

# 获取尺寸，获取内容文字，获取任意属性值
# size = driver.find_element_by_css_selector("#kw").size
# print(size)
# text = driver.find_element_by_css_selector("#jgwab").text
# print(text)
# href = driver.find_element_by_css_selector("#jgwab").get_attribute("href")
# print(href)

# 鼠标操作
# ActionChains类提供了鼠标操作的常用方法
# perform()执行所有ActionChains中存储的行为
# context_click()    右击
# double_click()     双击 ----其他查书吧，拖动悬停什么的太不常用了

# 右击
# right_click = driver.find_element_by_css_selector("#su")
# ActionChains(driver).context_click(right_click).perform()

# 悬停
# hover = driver.find_element_by_css_selector(".bri")
# ActionChains(driver).move_to_element(hover).perform()

# 键盘事件
# driver.find_element_by_css_selector("#kw").send_keys("abcde")
# time.sleep(2)
# # 退格键
# driver.find_element_by_css_selector("#kw").send_keys(Keys.BACK_SPACE)
# # 空格
# driver.find_element_by_css_selector("#kw").send_keys(Keys.SPACE)
# driver.find_element_by_css_selector("#kw").send_keys("1234")
# time.sleep(2)
# # 全选
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"a")
# # 回车来代替click
# driver.find_element_by_css_selector("#kw").send_keys(Keys.ENTER)
# # 其他按键请查书，包括空格，tab，esc，复制粘贴等

# 页面信息
# driver.title
# driver.current_url

# webDriverWait类提供等待方法，在设置时间内，每隔一段时间检测一次当前页面元素是否存在，存在是和超时两个回调
# 这一块看得不太仔细，可能需要重新查书，在4.7.1章

# 隐式等待
# implicitly_wait()，，通过一定市场的等待，页面上的元素如果还没有加载完成，就抛出异常。
# driver.implicitly_wait(10)

# 定位多个元素
# 把所有的find_element_by_xxx改成find_elements_by_xxx


# # 多窗口切换
# # 获得当前窗口句柄
# serach_handle = driver.current_window_handle
# # 新开一个窗口
# inputBar = driver.find_element_by_css_selector("#kw")
# inputBar.clear()
# inputBar.send_keys("kkk")
# driver.find_element_by_css_selector("#su").click()
# driver.implicitly_wait(5)
# driver.find_element_by_css_selector(".t a").click()
# driver.implicitly_wait(8)
# # 获得所有窗口句柄
# all_handle = driver.window_handles
# # 进入注册窗口
# for handle in all_handle:
# 	if handle != serach_handle:
# 		driver.switch_to.window(handle)
# 		print("search window")
# # 关闭一个窗口
# time.sleep(2)
# driver.close()

# alert处理
# switch_to_alert方法
# 具体见4.11

# 操作cookie
# 有这么几个方法add_cookie({name,"value"}),get_cookit(name),get_cookie(),delete_cookie(name,xuanxiang),delete_all_cokie
# def addCookitFromStr(str):
# 	cookie = {}
# 	strArr = str.split(";")
# 	for item in strArr:
# 		name = item.split("=")[0]
# 		if name[0] == " ":
# 			name = name[1:]
# 		value = item.split("=")[1]
# 		print(name)+'='+value
# 		print("-------------------")
# 		driver.add_cookie({'name':name,'value':value})
# addCookitFromStr("SINAGLOBAL=8935926639210.398.1468908161435; UOR=www.liaoxuefeng.com,widget.weibo.com,www.liaoxuefeng.com; login_sid_t=96bcdf8ddf849b995785bbaed26e1e12; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; YF-V5-G0=b4445e3d303e043620cf1d40fc14e97a; WBStorage=02e13baf68409715|undefined; _s_tentry=-; Apache=8353019643027.282.1490853249905; ULV=1490853249917:34:5:3:8353019643027.282.1490853249905:1490599198191; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFK5hPo_8NdHHIFa_QE1fC25JpX5K2hUgL.Foqp1KzNSonXehM2dJLoIE2LxKqL1-BL12-LxKqLBoeLB.BLxKqLBK-LBoM0MJLoqcet; SUHB=0D-FR_2eWALOk0; ALF=1522389258; SSOLoginState=1490853259; un=17612161483; wvr=6; YF-Page-G0=f0e89c46e7ea678e9f91d029ec552e92; WBtopGlobal_register_version=d55ace0a0a9bdd99")
# time.sleep(1)
# driver.refresh()


# 截图
# driver.get_screenshot_as_file("./a.jpg")



# test
# driver.find_element_by_css_selector("#kw").send_keys("t")





# driver.quit()