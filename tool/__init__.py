#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime

# 获取当前目录
def current_dir():
    return os.getcwd()

# 给定的路径是否是目录
def is_dir(d):
    if d == None:
        return os.path.isdir(current_dir())
    else:
        return os.path.isdir(d)

# 在当前目录创建目录
def mk_dir(n):
    if n == None:
        os.mkdir('New_Folder')
    else:
        os.mkdir(n)

# 获取系统名
def sys_name():
    return os.name

# 以当前时间戳为文件名
def filename_timestamp():
    now = datetime.now().timestamp()
    return int(now)

# 以当前时间(年月日时分秒)为文件名
def filename_datetime():
    now = datetime.now()
    return now.strftime('%Y%m%d%H%M%S')

# 获取html的标题
def web_title(d):
    #context = '<meta charset="utf-8"><title>系统学习Android自动化测试 -Java篇-慕课网实战</title><meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1"><meta name="renderer" content="webkit"><meta property="qc:admins" content="77103107776157736375" />'
    # 截取<title>***</title>作为网址的name
    linkre = re.compile("(?<=<title>).+?(?=</title>)")
    return linkre.findall(d)

def fib(max):
    print('000')
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
