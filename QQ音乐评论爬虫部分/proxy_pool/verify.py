"""
    检测模块
    从数据库总拿到所有的代理数据, 然后逐个检测
"""
import requests
from db import RedisClient  # 导入数据库模块
import concurrent.futures
from config import TEST_URL

# TEST_URL = 'https://www.baidu.com/'  # 测试代理的网址

client = RedisClient()  # 实例化对象


def verify_proxy(proxy):
    """
    传入一个代理, 检测次代理是否可用
    """
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    headers = {
        'Cookie': 'll="118164"; bid=Zk-WQ1VTECg; douban-fav-remind=1; __gads=ID=b6f7cdec79d34f36-224b89f1f9d000bc:T=1647261080:RT=1647261080:S=ALNI_MYcAlbbjMDI5qNSJWH5EGTPTZSL0w; viewed="10086742"; gr_user_id=1e2d9bf7-b9b1-43fa-a55d-22f99b31405b; __utmz=30149280.1660232257.8.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=VsTrSZ8RBIfSjOVPxmZ15uPmVFXqGcK8; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1662284252%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIwDdMtWNFYBdDPxsEyaIbau4PxvqE8mZCkctOmSSTqgjQ9t03ToKtfCXerBAv7WU%26wd%3D%26eqid%3D8789a59e0003d90c0000000362f52237%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.376705943.1647430719.1660232257.1662284253.9; __utmc=30149280; __utmt=1; dbcl2="242971362:ldG4rKfN3NA"; ck=dmFo; push_noty_num=0; push_doumail_num=0; __utmv=30149280.24297; __gpi=UID=000007012a1d0cc4:T=1656315855:RT=1662284304:S=ALNI_MZvUujI1y06QBScSSeNTXdMdnPelg; ct=y; _pk_id.100001.8cb4=8768747e39712780.1647430718.6.1662284335.1660232255.; __utmb=30149280.33.8.1662284334808',
        'Host': 'www.douban.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.douban.com/group/586674/discussion?start=25&type=new',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
    try:
        response = requests.get(url=TEST_URL, proxies=proxies, timeout=5)
        if response.status_code in [200, 204, 206, 302]:   # 通过响应体的状态验证代理是否可用
            # 如果请求成功,代理传进来的代理是可以用的; 如果代理可用, 调用数据库模块的 max() ,把可用的代理设置为100
            print('********代理可用********:', proxy)
            client.max(proxy)
        else:
            # 如果请求不成功,代理传进来的代理不是可以用的; 如果代理不可用, 调用数据库模块的 decrease() ,把可用的代理进行减分
            print('----请求状态码不合法----:', proxy)
            client.decrease(proxy)
    except Exception as e:
        # 如果引发了报错, 代表代理没有在规定的时间内请求到数据, 我们也认为此代理不可用
        client.decrease(proxy)
        print('------请求超时------:', proxy)

# 检测代理的速度比较慢, 多任务爬虫(多进程,多线程)
def verify_thread_pool():
    """线程池检测代理"""
    # 1.从数据库中拿到所有代理
    proxies_list = client.all()  # -- 列表
    # 2.用线程池检测每个代理
    print('##########--正在检测代理--##########')
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for proxy in proxies_list:
            executor.submit(verify_proxy, proxy)









if __name__ == '__main__':
    # proxy = ['1.196.177.160:9999', '1.196.177.180:9999', '1.196.177.254:9999',
    #          '1.197.203.189:9999','1.198.73.252:9999', '1.199.31.33:9999']
    #
    # for pro in proxy:
    #     verify_proxy(pro)

    verify_thread_pool()
