import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(1000,3))

print("Data info:\n",data.describe())
print("data[1]>3:\n",data[1][data[1]>3]) # 筛选出第1列中数值大于3的数据
print("any data>3:\n",data[(data>3).any(1)]) # 筛选出任意1列中数值大于3的数据