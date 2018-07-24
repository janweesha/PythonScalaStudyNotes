# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 23:55:41 2018

@author: Janwee
"""
def g(i):
    try:
        import urllib.request as r
        page_n=i*44
        page='&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&loc=%E7%9F%B3%E5%AE%B6%E5%BA%84&s={}'.format(page_n)
        url='https://s.taobao.com/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'+page+'&ajax=true'
        data=r.urlopen(url).read().decode('utf-8','ignore')
        
        import json
        data=json.loads(data)
        #a=json.dumps(data)
        
        def info(x):
            return data['mods']['itemlist']['data']['auctions'][x]
        def loc(x):
            return data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        def name(x):
            return data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        print('第{}页商品信息：\n'.format(i+1))
        f=open('淘宝石家庄电脑信息打印结果.csv','a',encoding='gbk')
        f.write('第{}页商品信息：\n'.format(i+1))
        for x in range(44):
            f=open('淘宝石家庄电脑信息打印结果.csv','a',encoding='gbk')
            f.write('商品名:'+str(name(x))+'发货地：'+str(loc(x))+'   ')
            print('第{}个商品信息已打印'.format(x+1))
            f.close()
        f=open('淘宝石家庄电脑信息打印结果.csv','a',encoding='gbk')
        f.write('\n\n')
    except Exception as err:
        print('打印失败')
for i in range(100):
    g(i)

