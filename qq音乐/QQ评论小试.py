
#coding:utf-8

import requests.sessions
import time

headers={
# "Authorization":"Bearer token值",
'origin':'https://y.qq.com',
'pragma':'no-cache',
'referer':'https://y.qq.com/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}
time_out=str(int(time.time()*1000))
url=f'https://u.y.qq.com/cgi-bin/musics.fcg?_={time_out}&sign=zzb4eff34abalqxf6ziyzui6rqncbvhta3b79435d'

data="""{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"method":"GetCommentCount","module":"GlobalComment.GlobalCommentReadServer","param":{"request_list":[{"biz_type":1,"biz_id":"319905785","biz_sub_type":0}]}},"req_2":{"module":"music.globalComment.CommentReadServer","method":"GetNewCommentList","param":{"BizType":1,"BizId":"319905785","LastCommentSeqNo":"","PageSize":25,"PageNum":0,"FromCommentId":"","WithHot":1}},"req_3":{"module":"music.globalComment.CommentReadServer","method":"GetHotCommentList","param":{"BizType":1,"BizId":"319905785","LastCommentSeqNo":"","PageSize":15,"PageNum":0,"HotType":2,"WithAirborne":1}}}"""
res=requests.post(url,headers=headers,data=data).json()
req1=res['req_2']['data']['CommentList']['Comments']
for req1_data in req1:
    user=req1_data['Nick']
    comment=req1_data['Content']
    print(user,comment)

# import js2py
# context=js2py.EvalJs()
# n_fun_url='ttps://y.qq.com/ryqq/js/runtime~Page.d818e9f2ba106c0d6f5f.js?max_age=2592000'
#
# n_fun=requests.sessions(n_fun_url).content.decode()#字符串
# context.execute(n_fun)
# t.data=data

# import js2py
# import requests
# context=js2py.EvalJs()
# session=requests.session()
# session.headers={
#     'referer': 'https://y.qq.com/n/ryqq/songDetail/001dGNKF3KlMu0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
# }
# big_js=session.get('https://y.qq.com/ryqq/js/vendor.chunk.f3acac6acb21ac5aaf67.js?max_age=2592000').content.decode()#字符串
# context.execute(big_js)
# print(f'dfsfsdf:{big_js}')
#
# vendor=session.get('https://y.qq.com/ryqq/js/runtime~Page.d818e9f2ba106c0d6f5f.js?max_age=2592000').content.decode()#字符串
# # 'Request URL: https://y.qq.com/ryqq/js/vendor.chunk.f3acac6acb21ac5aaf67.js?max_age=2592000'
# print(f'dfsfsdf:{vendor}')
#
# context.execute(vendor)
# context.execute( 'n(350).default')


