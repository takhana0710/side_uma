import requests
from lxml import etree

url = 'https://gamewith.jp/uma-musume/article/show/255035'  # gw 網址
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}

def Sp_SupportCard():  # 爬蟲-支援卡
    data = {}
    info = list()
    r = requests.get(url=url, headers=headers).text
    html = etree.HTML(r)
    support_table=html.xpath('//table[@class="sorttable"]/tr[*]')
    for i in support_table:
        sup_info=i.xpath('.//text()')
        if sup_info[0] == '名前':
            continue
        data['name'] = sup_info[0]
        data['link']=i.xpath('./td/a/@href')[0]
        data['run_method']=i.xpath('./td[2]//text()')[0]
        data['distance']=i.xpath('./td[2]//text()')[1:]
        data['distance']=",".join(data['distance'])
        data['rank']=i.xpath('./td[3]//text()')[0]
        data['attr']=i.xpath('./td[4]//text()')[0]
        data['score']=i.xpath('./td[5]//text()')[0]
        info.append(data.copy())  # 要先複製一份新增進去 list才不會互蓋資料
        data.clear()  # 清空
    return info
