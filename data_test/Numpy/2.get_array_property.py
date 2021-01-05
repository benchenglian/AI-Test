# 获取数组对象基本属性
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,5,9],[10,11,12]])
print("a.shape:",a.shape) # 输出数组或矩阵的结构，即行列数
print("a.dtype:",a.dtype) # 输出数组元素的数据对象类型
print("a.ndim:",a.ndim) # 输出数组的秩
print("a.size:",a.size) # 输出数组元素的个数