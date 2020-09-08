# 需求：爬取搜狗首页页面数据
import requests
if __name__ == '__main__':
    # step 1 :指定url
    url = 'https://sougou.com/'
    # step2: 发起请求
    response = requests.get(url=url)
    # step3: 获取响应的数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # step 4:持久化存储
    with open('./sougou.html', 'w', encoding='utf-8')as fp:
        fp.write(page_text)
    print('爬取完成！！！！')
