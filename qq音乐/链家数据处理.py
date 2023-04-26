import pandas as pd
import jieba
from matplotlib import pyplot as plt
from numpy import nan
file=r'F:\python下载文件\qq音乐\链家成交详情.xlsx'
# file=r'京东.csv'

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# data = pd.read_csv(file, engine='python', encoding='utf-8')
data = pd.read_excel(file)
print(data.head())
print('重复值数量:{}'.format(data[data.duplicated()].size))#重复数据个数
data.drop_duplicates()#删除重复数据
print(f'样本数量：{len(data)}')
print(data.dtypes)

def func(temp):
    if temp:
        return int(temp) * 10000

# data['价格(万)']=data['价格(万)'].map(func)

statistics = data.describe() #保存基本统计量
print(statistics)
def plt_barh():
    data.sort_values(by = '平均价格', inplace = True)
    # 绘制条形图
    plt.barh(y = range(data.shape[0]), # 指定条形图y轴的刻度值
            width = data['平均价格'],# 指定条形图x轴的数值
            # tick_label = data.Province,# 指定条形图y轴的刻度标签
            color = 'steelblue', # 指定条形图的填充色
           )
    plt.xlabel('平均金额(元)')
    plt.ylabel('样本数据')
    # 添加条形图的标题
    plt.title('二手房平均出售价格')
    plt.show()
plt_barh()
print(data.columns)#获取列的索引名称
def pieChart():
    result = data['c1'].unique()

    plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
    label = ['第一', '第二', '第三']  # 定义饼图的标签，标签是列表
    explode = [0.01, 0.2, 0.01]  # 设定各项距离圆心n个半径
    # plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
    values = [4, 7, 9]
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
    plt.title('2018年饼图')
    plt.savefig('./2018年饼图')
    plt.show()
pieChart()
