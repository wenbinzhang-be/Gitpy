import requests
import json
if __name__ == '__main__':
    # 1 指定url
    post_url = 'https://fanyi.baidu.com/'
    # 2 UA伪装，指定headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    # 3，post请求参数处理
    word = input('enter a word')
    data = {
        'kw': word
    }
    # 4，接受请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取相应数据：json方法返回的obj（只有当确认数据返回是json数据时，才能使用json（）,x-www-form-urlencoded; charset=UTF-8这是他的数据类型，所以不能使用json（））
    dic_obj = response.json()
    # 6 持久化存储
    filename = word + '.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!!')



