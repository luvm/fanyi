import requests
import json

def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        return False

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
while True:
    content = input('请输入翻译内容（输入‘q’退出程序）：')
    if content == 'q':
        print('退出成功')
        break
    elif check_contain_chinese(content):
        data = {
            'from': 'zh',
            'to': 'en',
            'query': '%s' % (content),
        }
    else:
        data = {
            'from': 'en',
            'to': 'zh',
            'query': '%s' % (content),
        }

    post_url = 'https://fanyi.baidu.com/basetrans'

    r = requests.post(post_url,data=data,headers=headers)
    dict_ret = json.loads(r.content.decode())
    ret = dict_ret['trans'][0]['dst']
    print('翻译结果是：',ret)