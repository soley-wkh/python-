# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/3 20:23
    file   : 05-readfile.py
    
"""
import time
from selenium import webdriver


def getFile(url):
    # 实例化一个浏览器驱动
    chrome = webdriver.Chrome()

    # 访问页面
    chrome.get(url)

    # 捕获元素

    title = chrome.find_element_by_xpath("//h3[@class='j_chapterName']").text
    print(title)

    file = open("斗罗大陆.txt", mode="a", encoding="utf-8")
    file.write(title + "\n")

    texts = chrome.find_elements_by_xpath("//div[@class='read-content j_readContent']/p")
    for t in texts:
        content = t.text
        file.writelines(content + "\n")
    file.close()

    time.sleep(1)
    next_url = chrome.find_element_by_xpath("//a[@id='j_chapterNext']").get_attribute("href")
    if next_url:
        chrome.close()
        getFile(next_url)
    else:
        chrome.close()
        return


if __name__ == '__main__':
    getFile("https://read.qidian.com/chapter/YvJ9Xu5KMv01/igSRlHML7Ukex0RJOkJclQ2")
