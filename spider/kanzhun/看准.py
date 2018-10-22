#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: duanwei
@license: Apache Licence 
@contact: 4064865@qq.com
@site: http://blog.csdn.net/dwshmilyss
@software: PyCharm
@file: 看准.py
@time: 2018/10/11 18:15
"""
import sys
from selenium import webdriver
import time

default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    sys.setdefaultencoding(default_encoding)
# 导入开发模块
import requests
from bs4 import BeautifulSoup
import os
from six.moves import urllib
import requests
import numpy as np
import pandas as pd


def func():
    pass


class Main():
    def __init__(self):
        pass


## 获得信息
def get_company_info(num, headers):
    driver = webdriver.Chrome(executable_path="D:/10000347/Downloads/chromedriver_win32/chromedriver.exe")
    ## 获得评价数据
    url = 'https://www.kanzhun.com/gsr' + str(num) + '.html?ka=com-blocker1-review'
    js = 'window.open("' + url + '")'
    driver.execute_script(js)
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    bsObj = BeautifulSoup(driver.page_source, "html.parser")
    tag = bsObj.find('div', attrs={'class': 'all_item'}).text.replace('\t', '').replace('\n', '').replace('(',
                                                                                                          ' ').replace(
        ')', ' ').split(' ')
    tag = tag[0:len(tag) - 1]
    this_tag = {tag[i * 2]: tag[i * 2 + 1] for i in np.arange(int(len(tag) / 2 - 1))}
    this_name = bsObj.find('div', attrs={'class': 'co_name t_center'}).text
    this_overal = float(bsObj.find('div', attrs={'class': 'res_box_star f_right'}).find('em').text)
    points = bsObj.find('ul', attrs={'class': 'score_rate clearfix'}).text.replace('\n', ' ').split()
    this_recommend = float(points[0][0:2]) / 100 * 5
    this_future = float(points[2][0:2]) / 100 * 5
    this_ceo = float(points[4][0:2]) / 100 * 5
    ## 获得CEO头像和公司logo
    ceo_pic = bsObj.find('div', attrs={'class': 'ceo_info'}).find('div').find('img').attrs['src']
    ceo_name = bsObj.find('div', attrs={'class': 'ceo_info'}).find('p').text
    head_logo = bsObj.find('div', attrs={'class': 'com_logo f_left'}).find('img').attrs['src']
    head_loc = 'D:/爬虫/看准/公司logo/' + this_name + '.jpg'
    ceo_loc = 'D:/爬虫/看准/CEOlogo/' + this_name + '.jpg'
    urllib.request.urlretrieve(head_logo, head_loc)
    urllib.request.urlretrieve(ceo_pic, ceo_loc)
    ## 获得面试难度
    url = 'https://www.kanzhun.com/gsm' + str(num) + '.html?ka=com-floater-interview'
    js = 'window.open("' + url + '")'
    driver.execute_script(js)
    time.sleep(2)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    bsObj = BeautifulSoup(driver.page_source, "html.parser")
    # req = urllib.request.Request(url, headers=headers)
    # html = urllib.request.urlopen(req)
    # print(html.read().decode('utf-8',errors="replace"))
    # print(html.read().decode('utf-8'))
    # bsObj = BeautifulSoup(html.read().decode('utf-8',errors="replace"), "html.parser")
    this_difficulty = float(bsObj.find('section', attrs={'class': 'interview_feel'}).find('em').text)
    this_feeling = bsObj.find('ul', attrs={'class': 'score_list'}).find_all('span', attrs={'class': 'percent'})
    this_feeling = [float(k.text.replace('%', '')) for k in this_feeling]
    this_feeling = (this_feeling[0] * 5 + this_feeling[1] * 3 + this_feeling[2] * 1) / 100
    ## 整合数据成为字典
    this_company = {'name': this_name, 'overal': this_overal, 'comments': tag[1], 'recommend': this_recommend,
                    'future': this_future, 'ceo': this_ceo, 'difficulty': this_difficulty, 'feeling': this_feeling}
    return this_company, this_tag, this_name


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'aliyungf_tc=AQAAAL9RTEGmEAUAyopBcGooBoROxiVN; __c=1539246303; W_CITY_S_V=0; AB_T=abva; __g=-; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1539246304; _f_k=reborn; __l=r=&l=%2F; isHasPushRecommentMessage=true; __t=7hRYpv9uzftQ9nt; pageType=3; t=7hRYpv9uzftQ9nt; thirtyMinutesCount=2; lastMessageId=41834860; JSESSIONID=""; __a=85139647.1539246303..1539246303.104.1.104.104; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1539252715',
        'Host': 'www.kanzhun.com',
        'Referer': 'https://www.kanzhun.com/gsr2080582.html?ka=com-blocker1-review',
        'X-Requested-With': 'XMLHttpRequest'
    }
    this_company, this_tag, this_name = get_company_info(2080582, headers=headers)
    print(this_company)
    print(this_tag)
    print(this_name)

    # ## 整体评分top15柱形图
    # company = pd.read_excel('company_info.xlsx')
    # company_overal = company.sort_values('overal', ascending=False)[0:15]
    # attr = company_overal['name']
    # v1 = round(company_overal['overal'], 2)
    # bar = Bar("整体评分TOP15", title_pos='center')
    # bar.use_theme('essos')
    # bar.add("", attr, v1, is_stack=False, xaxis_rotate=30, yaxis_min=3.7, is_label_show=True,
    #         xaxis_interval=0, is_splitline_show=False)
    # bar.render('整体评分TOP15.html')
    pass
