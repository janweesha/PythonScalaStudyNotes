def g(i,j):
    try:
        import urllib.request as r
        page_n=i*44
        city_l=('%E5%8C%97%E4%BA%AC','%E4%B8%8A%E6%B5%B7','%E5%B9%BF%E5%B7%9E','%E6%B7%B1%E5%9C%B3','%E6%9D%AD%E5%B7%9E','%E9%95%BF%E6%B2%99','%E9%95%BF%E6%98%A5','%E6%88%90%E9%83%BD','%E9%87%8D%E5%BA%86','%E5%A4%A7%E8%BF%9E')
        city=city_l[j]#'%E5%8C%97%E4%BA%AC'
        page='&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&loc={}&s={}'.format(city,page_n)
        url='https://s.taobao.com/search?q=%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'+page+'&ajax=true'
        data=r.urlopen(url).read().decode('utf-8','ignore')
        
        import json
        data=json.loads(data)
        a=json.dumps(data)
        
        #def info(x):
            #return data['mods']['itemlist']['data']['auctions'][x]
        #def loc(x):
            #return data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        #def name(x):
            #return data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        def price(x):
            return data['mods']['itemlist']['data']['auctions'][x]['view_price']
        def sales(x):
            return data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        print('第{}页商品信息：\n'.format(i+1))
        f=open('北京到大连价格.txt','a',encoding='utf-8')
        f.write(a+'\n')
        f.close()
    except Exception as err:
        print('打印失败')
for j in range(10):
    print('打印第{}个城市中'.format(j+1))
    for i in range(100):
        g(i,j)
