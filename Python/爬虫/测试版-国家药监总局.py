import requests
import json
if __name__ == '__main__':
    # 获取企业ID数据
    url1 = 'http://www.gov.cn/2016public/top.htm'
    headers = {
       'headers': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    id_list = []  # 用来存储数据
    all_detail_list = []  # 用来存储所有企业详情数据
    for page in range(1, 3):  # 遍历所有业中的公司
        page = str(page)
        # 封装了一个字典
        data = {
            'on': 'ture',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '',
            'applyName': '',
            'applySn': ''
        }
        json_ids = requests.get(url=url1, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
            print(id_list)
    # 接下来获取企业详情页
    post_url = 'http://www.gov.cn/fuwu/bm/yjj/tpaq.htm#1'
    for id in id_list:
        data = {
            'id': id
        }
        detail_list = requests.post(url=post_url, data=data, headers=headers).json()
        all_detail_list.append(detail_list)
        # 永久化存储
        fp = open('./yaojianju.json', 'w', encoding='utf-8')
        json.dump(all_detail_list, fp=fp, ensure_ascii=False)
        print('over!!!1')
