import csv
import random
import requests
import parsel
import concurrent.futures
import time
from selenium import webdriver
start = time.time()


def get_proxy():
    """获取代理的函数"""
    proxy_json = requests.get(
        url='http://tiqu.pyhttp.taolop.com/getip?count=9&neek=15872&type=2&yys=0&port=2&sb=&mr=2&sep=0&ts=1&ys=1&cs=1').json()
    # print('获取到的代理:', proxy_json)
    proxy = proxy_json['data'][0]['ip'] + ":" + str(proxy_json['data'][0]['port'])
    print('提取出来的代理:', proxy)
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    return proxies

#
headers = {
    'Host': 'nt.lianjia.com',
    'Referer': 'https://nt.lianjia.com/chengjiao/pg100/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}


def Obtain(url):  # 获取html
    urls = []
    res = requests.get(url).text  # proxies=get_proxy()
    selector = parsel.Selector(res)
    lis = selector.css('.listContent li')
    for li in lis:
        href = li.css('a::attr(href)').get()
        urls.append(href)
    return urls


# ['房屋名称','成交时间','价格(万)','平均价格','房屋户型','所在楼层','建筑面积','户型结构','套内面积','建筑类型','房屋朝向','建成年代','装修情况','建筑结构','供暖方式','梯户比例','配备电梯']
def resolve(url):  # 获取数据
    for href in Obtain(url):
        data_res = requests.get(href).text
        data = parsel.Selector(data_res)
        address = data.css('.deal-bread a:nth-child(5)::text').get().replace('二手房成交', '')
        # communityName = data.css('.communityName .info::text').get()
        title = data.css('.house-title .wrapper::text').get()
        TransactionHour = data.css('.house-title .wrapper span::text').get()  # 交易时间
        price = data.css('.dealTotalPrice i::text').get()
        unitPrice = data.css('.price b::text').get()
        houseType = data.css('.base .content  ul li:nth-child(1)::text').get().replace(' ', '')
        transactionOwnership = data.css('.base .content  ul li:nth-child(2)::text').get().replace(' ', '')
        constructionArea = data.css('.base .content  ul li:nth-child(3)::text').get().replace(' ', '')
        houseStructure = data.css('.base .content  ul li:nth-child(4)::text').get().replace(' ', '')
        innerArea = data.css('.base .content  ul li:nth-child(5)::text').get().replace(' ', '')
        buildingType = data.css('.base .content  ul li:nth-child(6)::text').get().replace(' ', '')
        yearOfCompletion = data.css('.base .content  ul li:nth-child(7)::text').get().replace(' ', '')
        renovationCondition = data.css('.base .content  ul li:nth-child(8)::text').get().replace(' ', '')
        buildingStructure = data.css('.base .content  ul li:nth-child(9)::text').get().replace(' ', '')
        heatingMethod = data.css('.base .content  ul li:nth-child(10)::text').get().replace(' ', '')
        theProportionOfTerracedHouseholds = data.css('.base .content  ul li:nth-child(11)::text').get().replace(' ', '')
        houseOrientation = data.css('.base .content  ul li:nth-child(12)::text').get().replace(' ', '')
        equippedWithElevator = data.css('.base .content  ul li:nth-child(13)::text').get().replace(' ', '')
        print(address, title, TransactionHour, price, unitPrice, houseType, transactionOwnership, constructionArea,
              houseStructure, innerArea, buildingType, yearOfCompletion, renovationCondition, buildingStructure,
              heatingMethod, theProportionOfTerracedHouseholds, houseOrientation, equippedWithElevator)
        with open('链家2.csv', 'a', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow(
                [address, title, TransactionHour, price, unitPrice, houseType, transactionOwnership, constructionArea,
                 houseStructure, innerArea, buildingType, yearOfCompletion, renovationCondition, buildingStructure,
                 heatingMethod, theProportionOfTerracedHouseholds, houseOrientation, equippedWithElevator])


def theeding(url):  # 多线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        end = time.time()
        print(f'共花费时间{end - start}s')
        e.submit(resolve, url)


#区域 = {'南通经济技术开发区','启东市','如东县','如皋市','崇川区','海安市','海门区','港闸区','通州区'}

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as e:  # 多进程
        area_list = ['nantongjingjijishukaifaqu', 'qidongshi', 'rudongxian', 'rugaoshi', 'chongchuanqu', 'haianshi',
                     'haimenqu', 'gangzhaqu', 'tongzhouqu']
        for area in area_list:
            for i in range(1, 100):
                print(f'------------第{i}页------------')
                url = f'https://nt.lianjia.com/chengjiao/{area}/pg{i}/'
                #https://nt.lianjia.com/chengjiao/nantongjingjijishukaifaqu/
                #https: // nt.lianjia.com / chengjiao / qidongshi /
                try:
                    e.submit(theeding, url)
                except:

                    continue
