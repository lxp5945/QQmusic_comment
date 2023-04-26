def data_first():
    data = {
        "comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8", "notice": 0,
                 "platform": "yqq.json", "needNewCode": 1, "uin": 0, "g_tk_new_20200303": 5381, "g_tk": 5381},
        "req_1": {"method": "GetCommentCount", "module": "GlobalComment.GlobalCommentReadServer",
                  "param": {"request_list": [{"biz_type": 1, "biz_id": "320315208", "biz_sub_type": 0}]}},
        "req_2": {"module": "music.globalComment.CommentReadServer", "method": "GetNewCommentList",
                  "param": {"BizType": 1, "BizId": "320315208", "LastCommentSeqNo": "", "PageSize": 25, "PageNum": 0,
                            "FromCommentId": "", "WithHot": 1}},
        "req_3": {"module": "music.globalComment.CommentReadServer", "method": "GetHotCommentList",
                  "param": {"BizType": 1, "BizId": "320315208", "LastCommentSeqNo": "", "PageSize": 15, "PageNum": 0,
                            "HotType": 2, "WithAirborne": 1}}}
    return data

#     data_first()
#     req2 = res['req_2']['data']['CommentList']['Comments']
#     for req2_data in req2:
#         user = req2_data['Nick']
#         comment = req2_data['Content']
#         print(user, comment)

import re
str="http://thirdqq.qlogo.cn/g?b=sdk&k=THyesm94szh10sMJBfw9xA&s=140&t=1555637733"
a=''.join(re.findall('.*?t=(.*)',str,re.S))
print(a)
