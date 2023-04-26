import pprint
import re
import json,time
import requests

headers={
    'origin':'https://y.qq.com',
    'pragma':'no-cache',
    'referer':'https://y.qq.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}
url='https://y.qq.com/n/ryqq/singer/004Be55m1SJaLk'
# url='https://y.qq.com/n/ryqq/singer/003fA5G40k6hKc'
res=requests.get(url,headers=headers)
# print(res.text)
sing_id=re.findall('.*?,"id":(\d\d\d\d+),"isonly"',res.text,re.S)
pprint.pprint(sing_id)
comment_time='54353553'
timeStamp=1639041362
timeArray = time.localtime(timeStamp)
print(timeArray)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

import execjs
import requests
import time,json
# "id":105648715,"isonly"
# 评论接口中的sign有加密，使用node获取js解密函数
# with open('./code2.js', encoding='utf8') as f:
# with open('code.js', encoding='utf8') as f:
#     js_func = execjs.compile(f.read())
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
#     'origin': 'https://y.qq.com',
#     'accept-encoding': 'gzip, deflate, br',
#     'referer': 'https://y.qq.com/',
#     'accept-language': 'zh-CN,zh;q=0.9',
# }
#
# data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.globalComment.CommentReadServer","method":"GetNewCommentList","param":{"BizType":1,"BizId":"102807914","LastCommentSeqNo":"1039205090197747200","PageSize":25,"PageNum":2,"FromCommentId":"","WithHot":0}}}
# p_data = json.dumps(data)# sign 加密
# sign = js_func.call('window.get_sgin', p_data)
# print('sign --> ',sign)
# params = (
#     ('_', '{}'.format(time.time() * 1000)),
#     ('sign', sign),
# )
# res = requests.post('https://u.y.qq.com/cgi-bin/musics.fcg', headers=headers, params=params, data=p_data).json()
# print(res)
# for comment in res['req_1']['data']['CommentList']['Comments']:
#     print(comment['Nick'],'-->',comment['Content'].replace('\n',''))


