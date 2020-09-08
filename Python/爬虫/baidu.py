import requests
url = 'https://www.baidu.com/?'
response = requests.get(url=url)
# print(response)
# print(response.encoding)
# 手动设定编码格式
# response.encoding = 'utf-8'
# print(response.text)
# # 打印源码的str类型数据
# # print(response.encoding)
# # response.content是存储的bytes类型的响应源码，可以进行decode操作
# print(response.content.decode())
#
# # 常见
# # 响应的url
# print(response.url)
# # 状态码
# print(response.status_code)
# # 响应头
# print(response.headers)
print(response.history)
import requests
import json

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    kw = input('enter a word')
    data = {
        'kw': kw
    }
    dic_obj = requests.post(url=url, data=data, headers=headers).json()
    fileName = kw + '.json'

    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('over!!!')
