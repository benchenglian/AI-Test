import numpy as np
from scipy import linalg

A = np.array([[1,2],[3,4]])

# |A| = det(A) = 1*4-2*3 = -2
# 计算方阵A的行列式
x = linalg.det(A)
print("A矩阵的行列式：",x)

# 计算方阵A的逆
iA = linalg.inv(A)
print("A矩阵的逆矩阵：",iA)

# 计算方阵A的特征值和特征向量
L,v = linalg.eig(A)
print("A的特征值：",L)
print("A的特征向量：",v)