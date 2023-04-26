#coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('链家2.csv')
print(data.head(5))
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']#中文
plt.rcParams['axes.unicode_minus'] = False
print('数据量{}'.format(len(data)))
statistics = data.describe()
print(statistics)
#重复数据个数
print('重复值数量:{}'.format(data[data.duplicated()].size))
#删除车位
print(data[data['房屋户型']== '车位'].index.tolist())
data_drop=data.drop(data[data['房屋户型']== '车位'].index.tolist())
print('删除异常值后样本量:{}'.format(len(data_drop)))
#众数替换未知数据
mode=data['建成年代'].mode().values[0]
print('建成年代众数:{}'.format(mode))

def date_time(item):#众数
    if item=='未知':
        return mode
    if item!='未知':
        return item
data['建成年代']=data['建成年代'].map(date_time)
median=data['总层数'].describe()[5]#中位数
#补充总层数缺失值
def nan_drop(item):
    if item:
        return median
data['总层数'] = data['总层数'].map(nan_drop)


#替换配备电梯的位置数据
data.loc[((data['配备电梯']=='暂无数据') & (data['总层数']<12)), '配备电梯'] = '无'
data.loc[((data['配备电梯']=='暂无数据') & (data['总层数']>=12)), '配备电梯'] = '有'

print(data.head(10))


#分组_柱状图

data_group_house=data_drop.groupby('房屋户型')
data_bar=data_group_house.count()['房屋名称']
data_bar=data_bar.sort_values()
# print(data_bar)

list_count=[]
list_col=[]
for row,count in data_bar.iteritems():
    list_count.append(count)
    list_col.append(row)
# print(list_count)
# print(list_col)
def plt_barh():
    # 绘制条形图
    plt.barh(y = list_col, # 指定条形图y轴的刻度值
            width = list_count,# 指定条形图x轴的数值
            color = 'green', # 指定条形图的填充色
           )
    plt.xlabel('样本量')
    plt.ylabel('房屋户型')
    plt.title('二手房房屋户型')
    data = pd.Series(list_count, index=list_col)
    x, y = data.index, data.values
    # for a, b in zip(x, y):
    #     plt.text(a, b - 0.3, '%.3f' % b, ha='center', va='bottom', fontsize=15)
    plt.show()
plt_barh()
# 绘制平均价格条形图
def plt_barh_price():
    data.sort_values(by = '平均价格', inplace = True)

    plt.barh(y = range(data.shape[0]), # 指定条形图y轴的刻度值
            width = data['平均价格'],# 指定条形图x轴的数值
            # tick_label = data.Province,# 指定条形图y轴的刻度标签
            color = 'steelblue', # 指定条形图的填充色
           )
    plt.xlabel('样本数量')
    plt.ylabel('样本数据')
    # 添加条形图的标题
    plt.title('二手房平均出售价格')
    plt.show()
plt_barh_price()
#修建年份
print(data.groupby(by='建成年代').count()['房屋名称'].values.tolist())
print(data.groupby(by='建成年代').count()['房屋名称'].index.tolist())
def plt_barh_time():
    data.sort_values(by = '建成年代', inplace = True)

    plt.barh(y = data.groupby(by='建成年代').count()['房屋名称'].index.tolist(), # 指定条形图y轴的刻度值
            width =data.groupby(by='建成年代').count()['房屋名称'].values.tolist() ,# 指定条形图x轴的数值
            color = 'red', # 指定条形图的填充色
           )

    plt.xlabel('平均金额(元)',fontsize=6)
    plt.ylabel('样本数据',fontsize=6)
    # 添加条形图的标题
    plt.title('二手房建成时间')
    plt.show()
plt_barh_time()

