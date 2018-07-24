# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:02:19 2018

@author: Janwee
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
d=open('school_id.txt')
school=d.readlines()
citys=[50,41,43]
d.close()
f=open('全国招生人数.txt','a',encoding='utf-8')
for sid in school:
    for city in citys:
        for ls in [1,2]:
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(sid,ls,city).encode(),headers=headers)
            data=r.urlopen(req).read().decode('utf-8','ignore')
            import json
            data=json.loads(data)
            a=json.dumps(data)
            f.write(a+'\n')
            print(school)
f.close()