# import requests
# import json
# if __name__ == '__main__':
#     url = 'https://movie.douban.com/'
#     headers = {
#         'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
#     }
#     data = {
#         'sort': 'U',
#         'range': '0, 10',
#         'tags': '',
#         'start': '0',
#         'genres': '爱情',
#         'countries': '中国大陆'
#     }
#      dict_data = requests.get(url=url, params=data, headers=headers).json()
#     fp = open('./douban.json', 'w', encoding='utf-8')
#     json.dump(dict_data, fp=fp, ensure_ascii=False)
#     print('over!!!')


