# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/3 17:37
    file   : 04-unittest_selenium使用.py
    
"""

import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner


class YouJiuYeTest(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def login(self, uname, passwd):
        username_dl = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_element_by_class_name("loginbutton1")
        username_dl.send_keys(uname)
        password_dl.send_keys(passwd)
        button.click()
        text = self.chrome.find_element_by_id("J_usernameTip").text
        return text

    def test_login_username(self):
        text = self.login("13333333333", "12345678")
        self.assertEqual('账号不存在', text, '提示内容有误')

    def test_login_password(self):
        text = self.login("13333333333", "123")
        self.assertEqual('密码应该为6-20位之间', text, '密码太短提示内容有误')

    def tearDown(self):
        time.sleep(5)
        self.chrome.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(YouJiuYeTest("test_login_username"))
    suite.addTest(YouJiuYeTest("test_login_password"))

    with open("test_report.html", "wb") as f:
        runner = HTMLTestRunner(
            stream=f,
            title='测试',
            description="就是一个测试"
        )
        runner.run(suite)
