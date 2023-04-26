"""
    调度模块
"""
from getter import proxies_func_list
from db import RedisClient
from verify import verify_thread_pool
from api import app
import time
import multiprocessing
from config import GETTER_PROXY, VERIFY_PROXY, SERVER_HOST, SERVER_PORT

client = RedisClient()


class Schedule:
    # 1. 调度获取代理的模块
    def getter_proxy(self):
        while True:
            for func in proxies_func_list:
                proxies = func()  # 对象
                for proxy in proxies:
                    client.add(proxy)
            time.sleep(GETTER_PROXY)  # 每五分钟抓取一次代理

    # 2. 调度验证代理的模块
    def verify_proxy(self):
        while True:
            verify_thread_pool()
            time.sleep(VERIFY_PROXY)

    # 3. 调用接口的模块
    def api_server(self):
        app.run(host=SERVER_HOST, port=SERVER_PORT)

    # 这三个方法需要一起去执行, 进程

    def run(self):
        print('##########--代理池开始运行--##########')
        # 把调度获取代理的函数转换为进程对象
        multiprocessing.Process(target=self.getter_proxy).start()

        # 把验证代理的函数转换为进程对象
        if client.count() > 0:
            multiprocessing.Process(target=self.verify_proxy).start()

        # 把调用接口的模块的函数转换为进程对象
        multiprocessing.Process(target=self.api_server).start()



if __name__ == '__main__':
    Schedule().run()
