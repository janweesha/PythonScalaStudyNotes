# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:36:10 2018

@author: 10257
"""
weather_dict={'day':('周一','周二','周三','周四','周五'),'temp':(23,25,26,28,24)}
for i in range(0,5):
    if(i!=2) :
        print(weather_dict["temp"][i])
    else:
        print(weather_dict["day"][i]+"温度是："+str(weather_dict["temp"][i]))


    

               
    
    
    

