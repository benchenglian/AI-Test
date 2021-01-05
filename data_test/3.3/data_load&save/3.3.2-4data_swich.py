import time

import numpy as np
import pandas as pd

data = pd.DataFrame({'name':['Wang Ning','LiMing','Sophie','Panis','Alice'],
                     'logintime':[1581001000,1581107100,1581051008,1582107105,1582104100],
                     'city':['Beijing','shanghai','paris','Rome','Tokyo'],
                     'gender':['female','Male','female','male','MALE']})
print("Data is:\n",data)

#把表示性别的单词统一转换为小写
data['gender'] = data['gender'].str.lower()
print("Data is:\n",data)

#把时间戳转换为日期
data['logintime'] = pd.to_datetime(data['logintime'],unit='s',origin=pd.Timestamp('1970-01-01 00:00:00'))

print("Data is:\n",data)

# now_time = time.time()
# format_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# print(type(format_date))
# print(type(now_time))
# print(type(data['logintime']))

# 添加列
# 先构建城市到国籍的映射
city_to_country = {
    'Beijing' : 'China',
    'shanghai' : 'China',
    'paris' : 'France',
    'Rome' : 'Italy',
    'Tokyo' :'Japan'
}

# 使用map方法获取映射值
data['nationality'] = data['city'].map(city_to_country)
print("Data is :\n", data)
