# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/3 17:03
    file   : 03-selenium使用.py
    
"""

from selenium import webdriver

# 实例化一个浏览器驱动
chrome = webdriver.Chrome()

# 访问页面
chrome.get("https://www.baidu.com/")

# 捕获元素
inputs = chrome.find_element_by_id("kw")

# 对元素进行
inputs.send_keys("李彦宏被泼水")

button = chrome.find_element_by_id("su")

button.click()

# 关闭浏览器
chrome.close()
