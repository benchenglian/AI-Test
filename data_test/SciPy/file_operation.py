# 文件操作
import numpy as np
from scipy import io as spio

data = np.ones((3,3))
spio.savemat('file.mat',{'a':data}) #以mat形式保存文件
data2 = spio.loadmat('file.mat',struct_as_record=True) # 加载mat文件
print(data2['a'])