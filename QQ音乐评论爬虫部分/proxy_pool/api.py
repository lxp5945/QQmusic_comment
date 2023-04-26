"""
    服务模块
    编写接口<地址>:  用户可以通过该接口拿到代理数据
        客户端访问服务器,拿到服务器数据
"""
import flask  # 到入flask框架  pip install flask
from db import RedisClient
from flask import request  # 获取地址的查询参数
from flask import jsonify  # 把对象转换成字符串

client = RedisClient()

# 实例化一个对象  app <application>
app = flask.Flask(__name__)


# http://www.ip3366.net/
# 视图函数: 提供服务的接口
@app.route('/')
def index():
    # 视图函数只能返回字符串数据
    return '<h2>欢迎来到代理池</h2>'


@app.route('/get')
def get_one():
    """随机获取一个代理, 需要调用数据库模块的 random() 方法"""
    one_proxy = client.random()
    return one_proxy


@app.route('/getcount')
def get_any_proxy():
    """指定数量获取代理, 需要调用数据库模块的 count_for_num() 方法"""
    num = request.args.get('num', '')
    if not num:  # 如果没有获取到查询参数  拿到的 num 数据类型是 str
        num = 1
    else:  # 获取到了查询参数
        num = int(num)

    any_proxy = client.count_for_num(num)  # 返回列表

    return jsonify(any_proxy)  # # 可以用json模块


@app.route('/getnums')
def get_nums():
    """获取当前数据库所有代理的数量, 需要调用数据库模块的 count() 方法"""
    count_proxy = client.count()
    return f'代理池目前还有 {count_proxy} 个代理可用!!!!'


@app.route('/getall')
def get_all():
    """获取当前数据库所有代理, 需要调用数据库模块的 all() 方法"""
    all_proxy = client.all()
    return jsonify(all_proxy)


if __name__ == '__main__':
    # 运行实例化的 app 对象
    app.run()
