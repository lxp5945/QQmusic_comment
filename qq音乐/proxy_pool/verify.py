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
