# -*- coding: UTF-8 -*-
# 网页解析器
import re

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print '获取所有链接'
links = soup.find_all('a')
for link in links:
    print link
    print link.name, link['href'], link.get_text()

print '获取单个链接'
link1 = soup.find('a', id="link2")
print link1

print '正则匹配'
link2 = soup.find('a', href=re.compile(r"ill"))
print link2

print '获取P段落文字'
link3 = soup.find('p', class_="title")
print link3
