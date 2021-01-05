import numpy as np
a = np.arange(10)
np.save("testNumpySave",a) #默认以未压缩的原始二进制格式保存在扩展名为.npy的文件中
b = np.load('testNumpySave.npy')
print(b)

a = np.arange(5)

np.savetxt('data.txt',a)
b = np.loadtxt('data.txt')
print(b)