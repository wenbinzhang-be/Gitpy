import requests
if __name__ == '__main__':
    # UA伪装：将对应的User-Agent凤凰钻到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83'
    }
    url = 'http://www.sougou.com/web'
    kw = input('enter a word')
    param = {
        'requery': kw
        }
    response = requests.get(url=url, params=param, headers=headers)  #

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8')as fp:
        fp.write(page_text)
    print(fileName, '保存成功')

