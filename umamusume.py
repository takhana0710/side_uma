import requests
from lxml import etree

url = 'https://gamewith.jp/uma-musume/article/show/253241'  # gw 網址
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}


def Sp_Umamusume():  # 爬蟲-馬娘角色
    data = {}
    info = list()
    r = requests.get(url=url, headers=headers).text
    html = etree.HTML(r)  # xpath 解析
    uma_table = html.xpath('//div[@class="umamusume-ikusei-ichiran"]/table/tr[*]')  # 取得所有表格資料
    for i in uma_table:
        table_info = i.xpath('.//text()')
        if table_info[0] == 'キャラ':  # 把表格 th 過濾
            continue
        data['name'] = table_info[0]  # 角色名字
        data['game_difficulty'] = table_info[1]  # 養成難度
        data['link'] = i.xpath('./td[2]/a/@href')[0]  # 培育論連結
        data['distance'] = i.xpath('./td[3]/div[@class="_inner-table"]/div[@class="_kyori"]//text()')  # 距離
        data['distance']=",".join(data['distance'])
        data['run_method'] = i.xpath('./td[3]/div[@class="_inner-table"]/div[@class="_sakusen"]//text()')  # 跑法
        data['run_method']=",".join(data['run_method'])
        attr = i.xpath('./td[4]/div[*]')
        attr_list = []
        for j in attr:
            if j.xpath('./img/@alt')[0] == 'スピードのアイコン':
                attr_list.append('speed%s' % j.xpath('./..//text()')[0])  # 返回父節點取加權數值
            elif j.xpath('./img/@alt')[0] == 'パワーアイコン':
                attr_list.append('power%s' % j.xpath('./..//text()')[0])
            elif j.xpath('./img/@alt')[0] == '根性のアイコン':
                attr_list.append('root%s' % j.xpath('./..//text()')[0])
            elif j.xpath('./img/@alt')[0] == 'スタミナのアイコン':
                attr_list.append('stamina%s' % j.xpath('./..//text()')[0])
            elif j.xpath('.//img/@alt')[0] == '賢さのアイコン':
                attr_list.append('smart%s' % j.xpath('./..//text()')[0])
        attr_list=",".join(attr_list)
        data['attr'] = attr_list
        # print(data)# 能力
        info.append(data.copy())  # 要先複製一份新增進去 list才不會互蓋資料
        data.clear()  # 清空
    return info
