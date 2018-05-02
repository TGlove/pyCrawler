# -*- coding: UTF-8 -*-
# 网页下载器
import cookielib
import urllib2

import bs4 as bs4

url = 'http://www.baidu.com'

print 'the first methord'

response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print 'the second methord'

request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5,0')

response2 = urllib2.urlopen(url)
print response2.getcode()
print len(response2.read())

print 'the third methord'

# 1 创建一个cookie容器
# 2 创建一个opener
# 3 以容器作为参数 创造一个handler 作为opener的参数
# 4 给URLlib2安装opener 此时URLlib2具有了cookie处理的增强能力


cj = cookielib.CookieJar()
open = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(open)

response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
# print response3.read()
