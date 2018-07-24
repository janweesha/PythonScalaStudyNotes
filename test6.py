# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 23:28:26 2018

@author: Janwee
"""

url='https://s.taobao.com/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)

sl=[]
def fee(x):
    return float(data['mods']['itemlist']['data']['auctions'][x]['view_fee'])
def name(x):
    return data['mods']['itemlist']['data']['auctions'][x]['title']
def price(x):
    return data['mods']['itemlist']['data']['auctions'][x]['view_price']
def free():
    for x in range(36):
        if fee(x)==0:
            print('商品名\n'+name(x)+'价格\n'+str(price(x))+'\n包邮')
            print('*'*80)
free()