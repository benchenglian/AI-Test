# 数据库数据

import sqlite3
import pandas as pd

query = "select * from user;"
con = sqlite3.connect('/Users/frank.lian/profile/docker-sqlite3/db/test.db')
cursor = con.execute(query)
data = cursor.fetchall() # 查询数据

print("data from db:\n",data)

# 把数据转换成DataFrame

df = pd.DataFrame(data,columns=[x[0] for x in cursor.description])
print("DataFrame is :\n",df)

# 数据清洗和准备
df.info()

print("df.shape:\n",df.shape) # 查看数据规模
print("df.dypes:\n",df.dtypes) # 查看数据类型
print("df.head:\n",df.head()) # 预览前五行
print("df.tail:\n",df.tail()) # 预览最后五行


# 数据类型转换
df['id'] = df['id'].astype(str) # 数值类型转换为字符串j
df['consumption'] = df['consumption'].str[1:].astype(float) # 字符串转数值类型
df['birthday'] = pd.to_datetime(df['birthday'],format='%Y-%m-%d') #字符串转换日期类型

print("data.dtypes:\n",df.dtypes)# 重新查看数据类型