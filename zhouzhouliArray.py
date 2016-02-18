# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 18:15:33 2015

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 00:35:24 2015

@author: xub
"""

from splinter.browser import Browser
from time import sleep

#用户名，密码
username = range(10)
passwd = range(10)
#分神
username[0] = "qqnum1"
passwd[0] = "pw1"
#飞雪映画
username[1]= "qqnum2"
passwd[1] = "pw2"
#叽里咕噜打呼噜
username[2]="qqnum3"
passwd[2]="pw3"

#网址
gift_url = "http://wuxia.qq.com/act/a20150914wxzzl/index.html"

def login():
    global b
    b = Browser(driver_name="chrome")
    for i in range(0,7):
        b.visit(gift_url)
        b.find_by_id("ptLoginBtn").click()
        sleep(3)
        with b.get_iframe('loginFrame') as iframe:
            iframe.find_by_id('u').fill(username[i])
            iframe.find_by_id('p').fill(passwd[i])
            iframe.find_by_id('go').click()
        sleep(3)
        b.find_by_tag("a")[2].click()
        sleep(4)
        b.find_by_xpath('//select[@id="area1ContentId_wuxia"]/option[@value="7609516"]')._element.click()
        sleep(3)
        b.find_by_xpath('//select[@id="areaContentId_wuxia"]/option[@value="2002"]')._element.click()
        sleep(3)
        b.find_by_id("confirmButtonId_wuxia").click()
        sleep(3)
        b.get_alert().dismiss()
        sleep(1)
        b.find_by_id("ptLogoutBtn").click()
        sleep(10)
    print u"领取完毕"
    sleep(3)

if __name__ == "__main__":

    login()
