import pandas as pd
import jieba
from matplotlib import pyplot as plt
from numpy import nan
file=r'F:\python下载文件\qq音乐\music_database.csv'

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(file, engine='python', encoding='utf-8-sig',)
print(data.head())
print(f'样本数量：{len(data)}')
statistics = data.describe() #保存基本统计量
def func(temp):
    if '万' in temp:
        return float(temp.strip('万')) * 10000
    return temp
data['attention'] = data['attention'].map(func)# 处理关注数量单位，万
print('重复值数量:{}'.format(data[data.duplicated()].size))#重复数据个数
data.drop_duplicates()#删除重复数据

def nan_drop():
    for star in data['singer']:#歌手为空，删除整行数据
        if not star.notnull():
            data.drop(axis=0,index='')
            pass
#[sing_name,singer,attention,user,otherStyleTime,comment]

def group():
    data_group_singer=data.groupby(['singer','singer'])#对歌手和歌曲进行分组
    print(data_group_singer.size())
    print(data_group_singer.count())
    for row, rowdata in data_group_singer.iteritems():
        print(row,rowdata)


def plt_barh():
    data.sort_values(by = 'GDP', inplace = True)
    # 绘制条形图
    plt.barh(y = range(data.shape[0]), # 指定条形图y轴的刻度值
            width = data.GDP,# 指定条形图x轴的数值
            tick_label = data.Province,# 指定条形图y轴的刻度标签
            color = 'steelblue', # 指定条形图的填充色
           )
    # 添加x轴的标签
    plt.xlabel('歌手姓名')
    # 添加条形图的标题
    plt.title('QQ音乐爬取歌手评论数量')
    # 为每个条形图添加数值标签
    for y,x in enumerate(data.GDP):
        plt.text(x+0.1,y,'%s' %round(x,1),va='center')
    plt.show()

