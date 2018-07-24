# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:30:16 2018

@author: 10257
"""

#打印每天18点的天气信息，
#写出英文版的app，天气情况，用户输入
#打印温度折线图‘ 
import urllib.request as r
url = "http://api.openweathermap.org/data/2.5/forecast?q=tongren,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
data = r.urlopen(url).read().decode('utf-8','ignore')

import json
data = json.loads(data)

A = [2,10,18,24,32]
temlist = []
for X in A:
    
    print(str(data['list'][X]['main']["temp"]))
    print(str(data['list'][X]['main']["pressure"]))
    print(str(data['list'][X]['main']["temp_max"]))
    print(str(data['list'][X]['main']["temp_min"])) 
    print(str(data["list"][X]["weather"][0]["description"]))
    m=str(data["list"][X]["weather"][0]["description"])
    if m.endswith('云') :print("the weather is good")
    else:print("the weather is prefect")
    
    
print("Varation of the temp")
m = int(len(data["list"]))
for i in A:
    print("*"*int(data['list'][i]['main']["temp"]))
print("====================")
print("sorted of the temp")
for i in A:
    temlist.append((data['list'][i]['main']["temp"]))
sorted(temlist)
print(temlist)
print("====================")



    


        
   
