import time

import scrapy


class GainCommentSpider(scrapy.Spider):
    name = 'gain_comment'
    allowed_domains = ['y.qq.com']
    # start_urls = ['https://y.qq.com/n/ryqq/singer/003fA5G40k6hKc']
    def start_requests(self):
        # scrapy.FormRequest()  是scrapy框架封装的发送 post 请求的方法
        localtime=time.time() * 1000

        yield scrapy.FormRequest(url=f'https://u.y.qq.com/cgi-bin/musics.fcg?_={localtime}&sign=zzb34c75a00kcqytomrli9l2drjydg2f9040fa',
                                 headers={ 'origin':'https://y.qq.com',
                                            'pragma':'no-cache',
                                            'referer':'https://y.qq.com/',
                                            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
},
                                 formdata={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.globalComment.CommentReadServer","method":"GetNewCommentList","param":{"BizType":1,"BizId":"127524204","LastCommentSeqNo":"1051427141058772992","PageSize":25,"PageNum":1,"FromCommentId":"","WithHot":0}}},

                                 # formdata={
                                 #    'cname':'',
                                 #    'pid':'',
                                 #    'keyword': '北京',
                                 #    'pageIndex': '1',
                                 #    'pageSize': '10'
                                 # },
                                 callback=self.parse,
                                 # meta={'page': 2}  # 用于scrapy框架中函数与函数间的数据传递
                                 )


    def parse(self, response):
        print(response.text)
        res_json = response.json()['req_1']['data']['CommentList']['Comments']
        # print(res_json)
        # req1 = res_json
        for req1_data in res_json:
            user = req1_data['Nick']
            comment = req1_data['Content'].replace('\n', ';')
            seqno = req1_data['SeqNo']
            PubTime = req1_data['PubTime']  # 时间戳
            timeArray = time.localtime(PubTime)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            yield {
                'user':user,
                'otherStyleTime':otherStyleTime,
                'comment':comment,
            }
        pass
