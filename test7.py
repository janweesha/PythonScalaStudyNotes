# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:45:52 2018

@author: 10257
"""

##1
import random
def Temp(a):
    if a<=10:
        print("请注意保暖，今天天气较低")
    elif a>10&a<=20:
        print("今天天气适合郊游")
    elif a>20&a<=30:
        print("今天天气适合外出")
    else:
        print("天气炎热，注意防晒")
temp= random.randint(1,40)
use = input("请输入今天天气：")
print(int(use))
Temp(int(use))
##2
import urllib.request as r
import json

url = "https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true"
data = r.urlopen(url).read().decode('utf-8','ignore')
data = json.loads(data)
for i in range(35):
    if i ==5:break
    if i ==10:continue
    print("price ="+ data["mods"]["itemlist"]["data"]["auctions"][i+1]["view_price"])  
    print("title =" + data["mods"]["itemlist"]["data"]["auctions"][i+1]["raw_title"])
    print("sale ="+ data["mods"]["itemlist"]["data"]["auctions"][i+1]["view_sales"])    
    if (i+1)%4==0:
        print("=============================")