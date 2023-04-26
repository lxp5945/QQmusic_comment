"""
项目配置文档
"""

"""项目配置(常量)"""


"""数据库配置"""
REDIS_HOST = '127.0.0.1'        # 数据库所在的ip地址
REDIS_PORT = 6379               # 数据库所在的端口
REDIS_DATABASE = 0              # 操作哪一个数据库

REDIS_OBJECT = 'PROXIES'        # 数据库操作对象

"""时间间隔配置"""
GETTER_PROXY = 60 * 10           # 获取代理的时间间隔
VERIFY_PROXY = 60 * 3           # 获取验证代理的时间间隔

"""服务器配置"""
SERVER_HOST = '127.0.0.1'       # api服务的地址
SERVER_PORT = 5000              # api服务端口

"""测试地址"""
TEST_URL = "'https://www.douban.com/group/586674/discussion'"   # 测试url
# TEST_URL = "'https://y.qq.com/n/ryqq/songDetail/002TsjSY3dWAz5'"   # 测试url

"""数据库分数设置"""
INIT_SCORE = 10     # 初始分数
HIGH_SCORE = 100    # 最高分数
MINIMUM_SCORE = 1     # 最低分数
HIGHEST_SCORE = 99    # 范围指定

"""分数操作"""
CHANGE_SCORE = -1

"""页码"""
PAGE=20

