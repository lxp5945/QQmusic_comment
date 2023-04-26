# import time
# import requests
# from selenium import webdriver
#
# selenium_url='https://nt.lianjia.com/ershoufang/'
#
# driver=webdriver.Chrome()
#
# driver.get(selenium_url)
# time.sleep(10)
# driver.implicitly_wait(15)
# driver.find_element_by_css_selector('.geetest_radar_tip').click()
# time.sleep(3)
# src=driver.find_element_by_css_selector('.geetest_item_wrap img::attr(src)')
#
#
# res = requests.get(src).content
# with open('img_2.jpg','wb') as f:
#     f.write(res)
#
# driver.quit()

area_list = ['nantongjingjijishukaifaqu', 'qidongshi', 'rudongxian', 'rugaoshi', 'chongchuanqu', 'haianshi',
                     'haimenqu', 'gangzhaqu', 'tongzhouqu'][0:3]
print(area_list)