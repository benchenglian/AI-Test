import numpy as np

a = np.array([[1,3,2],[4,8,5],[7,6,9]])
print("a:\n",a)
index = a.argmax(axis=0) # 获取每一列最大值的索引
print("index:\n",index)

a_max = a[index,range(a.shape[1])] #输出每列的最大值
print("a_max:\n",a_max)
print("sort:\n",np.sort(a,axis=1)) # 每行元素按照从小到大进行排序
print("argsort:\n",np.argsort(a)) # 返回数组从小到大的索引值