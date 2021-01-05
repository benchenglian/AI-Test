import pandas as pd
scores = [34,65,78,12,98,87]
grades = [0,60,80,90,100]
data = pd.cut(scores,grades) #按成绩拆分
print("Data is :\n",data)

# categories和codes，分别表示不同名称的类型数组和相应的数据分组编号。
print("Data.categories:\n", data.categories)

print("Data.codes:\n",data.codes)

#使用value_counts()函数统计数据落在各个区间的情况

print("value counts:\n",pd.value_counts(data))

#使用cut的labels设置分组的名称
print("Use Lables:\n",pd.cut(scores,grades,labels=['D','C','B','A']))