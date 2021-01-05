# 创建数组

import numpy as np

# 创建指定大小、数据类型但未初始化的数组，数组元素是int类型的随机值
a = np.empty([3,4],dtype = int)
print("empty array :\n" ,a)

# 创建指定大小的数组，数组元素均为float类型的0
a = np.zeros([2,2],dtype = float)
print("zeros array: \n",a)

# 创建指定大小的数组，数组元素均为int类型的1
a = np.ones([2,2],dtype = int )
print("ones array:\n",a)

# 创建N维数组对象
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("array:\n",a)

# 从已有数组或元组创建数组
x = [(1,2,3),(4,5,6)]
a = np.asarray(x)
print("asarray:\n", a)

# 从数值范围创建数组
a = np.arange(start=1,stop=6,step=2)
print("arange array: \n",a)

# 创建随机元素数组
a = np.random.random([2,3]) # 创建2*3的随机数组矩阵，random即用来创建[0,1)的随机数
print("random array:\n",a)

#用linspace创建一维等差数组(介于0～20，共11个元素)
a = np.linspace(start=0,stop=20,num=11)
print("linspace array:\n",a)

# 用logspace创建等比数组(介于base^start~base^stop),包含base^stop,共生成num个元素
a = np.logspace(start=1,stop=3,num=3,endpoint=True,base=2)
print("logspace array:\n",a)
