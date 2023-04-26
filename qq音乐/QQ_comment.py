import csv
import json
import pprint
import re
import execjs
import requests
import parsel
import time
import concurrent.futures

headers={
    'origin':'https://y.qq.com',
    'pragma':'no-cache',
    'referer':'https://y.qq.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}
def respose():#获取歌手页面
    url='https://y.qq.com/n/ryqq/singer_list?index=-100&genre=-100&sex=-100&area=200'
    res=requests.get(url,headers=headers).text
    return res


def resolve():#获取歌曲信息
    res = respose()
    selector = parsel.Selector(res)
    lis = selector.css('.singer_list_txt li')
    # sing_name_list = []
    # singer_name_list = []
    # sing_href_list = []#歌手详情页
    information_all_list = []
    num_time = 0
    for li in lis:
        name=li.css('a::text').get()
        href=li.css('a::attr(href)').get()
        href = 'https://y.qq.com'+href#有评论页面的链接
        singer_res=requests.get(href).text
        sing_id_list = re.findall('.*?,"id":(\d\d\d\d+),"isonly"', singer_res, re.S)
        print(sing_id_list)
        sing_html = parsel.Selector(singer_res)
        lis=sing_html.css('.songlist__list li')
        num=0
        for li in lis:
            num_time+=1
            sing_name=li.css('.songlist__songname_txt a::text').get()
            sing_href='https://y.qq.com'+li.css('.songlist__songname_txt a::attr(href)').get()

            attention = sing_html.css('.data__cont .data__actions .mod_btn span::text').get()
            # print(name, sing_name,attention,sing_href)
            with open('歌曲.csv','a',encoding='utf-8') as f:
                f.write('|'.join([name, sing_name,attention,sing_href])+'\n')
            sing_id=sing_id_list[num]
            information_tuple=(sing_name,name,attention,sing_href,sing_id,)
            num+=1
            information_all_list.append(information_tuple)
    if num_time>=10:
        return information_all_list

def data_last(BizIds,page,LastCommentSeqNo=""):

    data = {
        "comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8", "notice": 0,
                 "platform": "yqq.json", "needNewCode": 1, "uin": 0, "g_tk_new_20200303": 5381, "g_tk": 5381},
        "req_1": {"module": "music.globalComment.CommentReadServer", "method": "GetNewCommentList",
                  "param": {"BizType": 1, "BizId": f"{BizIds}", "LastCommentSeqNo": f"{LastCommentSeqNo}",
                            "PageSize": 25, "PageNum": int(f'{page}'), "FromCommentId": "", "WithHot": 0}}}
    return data


def sign_gain(data):
    with open('code.js', encoding='utf8') as f:
        js_func = execjs.compile(f.read())

    p_data = json.dumps(data)  # sign 加密
    sign = js_func.call('window.get_sgin', p_data)
    print('sign --> ', sign)
    url = f'https://u.y.qq.com/cgi-bin/musics.fcg'
    params = (
        ('_', '{}'.format(time.time() * 1000)),
        ('sign', sign),
    )
    res = requests.post(url, headers=headers, params=params, data=p_data)
    return res


def getComments(information):#获取评论数据

        BizIds = information[4]  # 歌曲标识id
        datas = data_last(BizIds,1)
        sing_name=information[0]
        star_name=information[1]
        attention=information[2]
        for page in range(2,8):#前4页评论
            res = sign_gain(datas)
            selector_comment_html=parsel.Selector(res.text)
            publishTime=''.join(selector_comment_html.css('.data__info li:nth-child(5)::text').getall()).replace('\n','')#发行时间
            res_json=res.json()
            # print(res_json)
            req1=res_json['req_1']['data']['CommentList']['Comments']
            a=0
            for req1_data in req1:
                user = req1_data['Nick']
                comment = req1_data['Content'].replace('\n',';')
                seqno=req1_data['SeqNo']
                if req1_data['PubTime']:
                    PubTime=req1_data['PubTime']#时间戳
                    timeArray = time.localtime(PubTime)
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print(sing_name,star_name,attention,publishTime,user,otherStyleTime,comment)
                with open('QQ音乐评论文件.csv', 'a', encoding='utf-8', newline='') as f:
                    write = csv.writer(f)
                    write.writerow([sing_name, star_name, attention, user, otherStyleTime, comment])
                a=a+1
                if a>=25:
                    print(seqno)
            datas = data_last(BizIds,page,LastCommentSeqNo=seqno)


def threed(information):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        # information_list_tuple = resolve()
        #
        # for information in information_list_tuple[0:2]:  # 歌曲数量()
        e.submit(getComments,information)


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as e:
        information_list_tuple = resolve()
        for information in information_list_tuple:  # 歌曲数量()
            e.submit(threed,information)



