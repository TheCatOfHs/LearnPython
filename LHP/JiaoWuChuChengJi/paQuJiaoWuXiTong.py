# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 16:58:24 2017

@author: vento
"""

import urllib
import urllib2
import cookielib
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Tkinter import *
import tkMessageBox

    
class CUMT:
    
    def __init__(self):
        
        #三个网址，第一个网址是登陆教务系统网站，
        #第二个网址是进入到查看学生成绩信息页面，
        #第三个网址是点击“查询后”跳出学生成绩的页面，也是我们抓取成绩的页面
        self.loginUrl = 'http://202.119.206.62/xtgl/login_login.html'
        self.gradeUrl = 'http://202.119.206.62/cjcx/cjcx_cxDgXscj.html'
        self.findUrl = 'http://202.119.206.62/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdmKey=N305005&sessionUserKey=10154236'

        #建立登陆的cookis
        self.cookies = cookielib.CookieJar()

        #将“和网页交流”所需要提供的数据存在字典中并转化为数据
        #每打开一个新的网页就需要提供新的交流的数据，称为request
        self.postdata1 = urllib.urlencode({
                'yhm':'10154236',
                'mm':'18103X'
                })
        self.postdata2 = urllib.urlencode({
                'gnmkdm':'N305005',
                'dyym':'/cjcx/cjcx_cxDgXscj.html',
                'gnmkmc':'%E5%AD%A6%E7%94%9F%E6%88%90%E7%BB%A9%E6%9F%A5%E8%AF%A2',
                'sfgnym':'1',
                'layout':'func-layout',
                'gnmkdmKey':'index',
                'sessionUserKey':'10154236'
                })
        self.postdata3 = urllib.urlencode({
                'xnm':'2016',
                'xqm':'12',
                '_search':'false',
                'nd':'1499174301704',
                'queryModel.showCount':'15',
                'queryModel.currentPage':'1',
                'queryModel.sortName':'',
                'queryModel.sortOrder':'asc',
                'time':'0'
                })

        #将cookie打开，并建立一个可以打开网页的opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        
    def getPage(self):

        #Request是用来和网页进行交流的函数，有两个参数：url和data，url是你要交流的网页，data是你要发送的数据
        #返回的结果request1指的是交流以后网页返回给你的数据（网页框架）
        request1 = urllib2.Request(
                url = self.loginUrl,
                data = self.postdata1)
        #用带有cookie的opener打开网页框架，转化为可以看懂的代码，可以成为“解读”
        result = self.opener.open(request1)
        
        #同上
        request2 = urllib2.Request(
                url = self.gradeUrl,
                data = self.postdata2)
        result2 = self.opener.open(request2)
        
        #同上
        request3 = urllib2.Request(
                url = self.findUrl,
                data = self.postdata3)
        result3 = self.opener.open(request3)

        #将带有学生成绩的解读的网页框架，作为函数的返回值
        return result3.read()
    
    def extractPage(self):
        #调用读取网页框架的函数，getPage的返回值就是result
        result = self.getPage()

        #利用正则表达式提取出你想要的内容，每个(.*?)代表你想要的内容，这里是声明正则表达式
        pattern = re.compile(r'"cj":"(.*?)","jd":"(.*?)".*?"kcmc":"(.*?)",.*?"xf":"(.*?)"', re.S)

        #从网页框架中对内容进行提取，即items
        items = re.findall(pattern, result)

        #将items作为函数返回值
        return items
        
            
    def sendEmail(self):
        #得到了上面这个函数的，你想要的内容
        items = self.extractPage()

        myGrade =[]
        for item in items:
            myGrade.append('\n课程名称：'+str(item[2])+
                           '\n学分为：'+str(item [3])+
                           '\n你的成绩为：'+str(item[0])+
                           '\n绩点为：'+str(item[1]))
            
        allGrade = 'Hi, 梁汉普！'
        for i in range(len(items)):
            allGrade = allGrade + myGrade[i]
        
        if len(items) == 3:
            print '还没出成绩！！！'

        else:
            mail_user="798258079@qq.com"    
            mail_pass="zhlnhujzeyujbdhe"   

            sender = '798258079@qq.com'
            receivers = ['798258079@qq.com']
            
            message = MIMEText(allGrade, 'plain', 'utf-8')
            message['From'] = Header('梁汉普的自动检查系统！', 'utf-8')
            message['To'] = Header('同学们', 'utf-8')
            
            subject = '教务系统发邮件啦！！！'
            message['Subject'] = Header(subject, 'utf-8')
            
            try:
                smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
                smtpObj.login(mail_user, mail_pass)  
                smtpObj.sendmail(sender, receivers, message.as_string())
                print '邮件发送成功'
            except smtplib.SMTPException, e:
                print '无法发送邮件！', e
                    

cumt = CUMT()
cumt.sendEmail()
