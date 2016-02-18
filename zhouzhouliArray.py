# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 00:35:24 2015

@author: toto233
"""

from splinter.browser import Browser
from time import sleep

#用户名，密码
username = range(10)
passwd = range(10)
#user1
username[0] = "qqnum1"
passwd[0] = "pw1"
#user2
username[1]= "qqnum2"
passwd[1] = "pw2"
#user3
username[2]="qqnum3"
passwd[2]="pw3"

#网址
gift_url = "http://wuxia.qq.com/act/a20150914wxzzl/index.html"

def login():
    global b
    b = Browser(driver_name="chrome")
    for i in range(0,3):
        b.visit(gift_url)
        b.find_by_id("ptLoginBtn").click()
        sleep(1)
        with b.get_iframe('loginFrame') as iframe:
            iframe.find_by_id('u').fill(username[i])
            iframe.find_by_id('p').fill(passwd[i])
            iframe.find_by_id('go').click()
        sleep(1)
        b.find_by_tag("a")[2].click()
        sleep(1)
        #大区，需要改成自己的，这是大地飞鹰
        b.find_by_xpath('//select[@id="area1ContentId_wuxia"]/option[@value="7609516"]')._element.click()
        sleep(1)
        #服务器，需要改成自己的，这是藏锋谷
        b.find_by_xpath('//select[@id="areaContentId_wuxia"]/option[@value="2002"]')._element.click()
        sleep(1)
        b.find_by_id("confirmButtonId_wuxia").click()
        sleep(1)
        b.get_alert().dismiss()
        sleep(1)
        b.find_by_id("ptLogoutBtn").click()
        sleep(5)
    print u"领取完毕"
    sleep(3)

if __name__ == "__main__":

    login()
