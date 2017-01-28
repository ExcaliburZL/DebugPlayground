#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import re
import tool
from collections import deque

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

queue  = deque()
visited = set()#防止爬了同一页面

url = 'http://www.imooc.com'
queue.append(url)
cnt = 0

while queue:
    url = queue.popleft() # 队首元素出队
    visited |= {url} # 标记为已访问

    print('已经抓取: ' + str(cnt) + ' 正在抓取 <--- ' + url)
    cnt += 1

    #抓取网页
    req = urllib.request.Request(url, headers=headers)
    urlop = urllib.request.urlopen(req)
    #判断是否为html页面
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    # 避免程序异常中止, 用try..catch处理异常
    try:
        #转换为utf-8码
        data = urlop.read().decode('utf-8')
        print(tool.web_title(data))
        # with open('test.html', 'w') as f:
        #     f.write(data)
    except:
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile("href=['\"]([^\"'>]*?)['\"].*?")
    ##返回所有有匹配的列表
    for x in linkre.findall(data):
        ##判断是否为http协议链接，并判断是否抓取过``
        if ('http' in x and x not in visited ) | ('https' in x and x not in visited ):
            queue.append(x)
            print('加入队列 ---> ' + x)
