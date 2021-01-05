import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,5,9],[10,11,12]])
print("a:\n",a)

# 数组元素值类型转换
b = a.astype(float)
print("a.dtype:",a.dtype,"b.dtype",b.dtype)

# 调整数组大小
print("a.reshape:\n",a.reshape(3,4))

# 获取数组元素
print("a[0:2]:\n",a[0:2]) # 获取数组前两行数据
print("a[:,2]:\n",a[:,2]) # 获取数组第3列数据

# 数组元素加/减/乘/除、判断
print("a+1:\n",a+1) # 对数组每个元素都统一加一
print("a**2:\n",a**2) # 对数组每个元素都求平方
print("a==5:\n",a==5) # 对数组元素逐一进行操作，判断是否等于5

# 数组元素求和
print("a按列求和:\n",a.sum(axis=0)) #按列求和
print("a按行求和:\n",a.sum(axis=1)) #按行求和

# 矩阵相关运算
A = np.array([[1,1],[0,1]])
B = np.array([[1,2],[3,4]])
print("A:\n",A)
print("B:\n",B)
print("A*B:\n",A*B) # 矩阵对应位置的元素相乘
print("A.dot(B):\n",A.dot(B)) # 计算矩阵内积
print("np.dot(A,B):\n",np.dot(A,B)) # 矩阵的乘法
print("A的扩展:\n",np.tile(A,(2,3))) # 矩阵扩展
