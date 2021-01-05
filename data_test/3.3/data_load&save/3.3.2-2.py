# 处理缺失数据
import pandas as pd
data = pd.read_csv('ex3.csv')
print("data is :\n",data)
print("data is null? \n",data.isnull()) #判断数据是否确实

print("去除包含缺失值的数据:\n",data.dropna())
print("去除有缺失值的列:\n",data.dropna(axis=1))

print("用0填充缺失值：\n",data.fillna(0))
print("用字典填充缺失值:\n",data.fillna({"年龄":"--","职业":"未知"}))