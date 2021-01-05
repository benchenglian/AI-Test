import numpy as np
import pandas as pd
'''
创建数据
'''
# 使用列表创建序列
s1 = pd.Series([1,2,3,4,5])
print("Series内容:\n",s1)
print("Series索引:\n",s1.index)
print("Series的值:\n",s1.values)

# 使用字典创建序列
mydic = {"a":1,"b":2,"c":3}
s2 = pd.Series(mydic, index=["a","c"])
print("Series2:\n",s2)

# 通过序列创建DataFrame
df1 = pd.DataFrame(s1,columns=['numbers']) # 指定列表
print("DataFrame1:\n",df1)

# 用序列对象生成 DataFrame
df2 = pd.DataFrame({'A':1,'B':pd.Series([1,2,3]),'c':pd.Timestamp('20200202'),'D':'Hello'})
print("DataFrame2:\n",df2)

# 通过Numpy数组创建 DataFrame
df = pd.DataFrame(np.array([[1,2],[3,1],[5,6],[7,2]]),columns=['A','B'],index=[2,3,4,5])
print("DataFrame3:\n",df)

'''
查看数据
'''
print("df.describe():\n",df.describe()) # 数据统计概要
print("df.head():\n",df.head(2))         # 头部数据预览
print("df.tail(3):\n",df.tail(2))       # 尾部数据预览
print("df.index:\n",df.index)           # 显示数据索引
print("df.columns:\n",df.columns)       # 显示数据列名

'''
数据排序
'''
print("df.sort_index:\n",df.sort_index(axis=1,ascending=False)) # 按轴排序
print("df.sort_values:\n",df.sort_values(by='B',ascending=False)) # 按值排序

'''
获取数据
'''
print("df['A']:\n",df['A']) # 按列获取内容
print("df[0:3]:\n",df[0:3]) # 切片操作
print("df.loc:\n",df.loc[:4,:'B']) # 还用loc索引器，基于行列标签获取数据
print("df.iloc:\n",df.iloc[:2,:2]) # 使用iloc索引器，基于行列索引获取数据

'''
数据计算
'''
print("df:\n",df)
print("df.add(1):\n",df.add(1))
print("df.mean():\n",df.mean()) # 获取数据每一列的均值
print("df.mean(1):\n",df.mean(1)) #获取数据每一列的均值
print("df.apply:\n",df.apply(lambda x:x.max() - x.min())) # apply函数

'''
文件操作
'''
df.to_csv('data.csv') # 写入csv文件
df2 = pd.read_csv('data.csv') # 读取csv文件
print("df2\n",df2)
df.to_excel('data.xlsx',sheet_name = 'sheet1') # 写入Excel
df3 = pd.read_excel('data.xlsx','sheet1') #读取Excel
print('df3\n',df3)
