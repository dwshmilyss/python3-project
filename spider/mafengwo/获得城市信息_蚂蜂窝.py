#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: duanwei
@license: Apache Licence 
@contact: 4064865@qq.com
@site: http://blog.csdn.net/dwshmilyss
@software: PyCharm
@file: 获得城市信息_蚂蜂窝.py
@time: 2018/10/15 18:41
"""
import sys
import os
from urllib.request import  urlopen
from urllib  import request
from bs4 import BeautifulSoup
import pandas as pd
from pyecharts import Bar,Geo

projectPath = os.path.abspath(os.path.dirname(sys.argv[0]))
print(projectPath)
print(os.getcwd())

# os.chdir(projectPath+"/")