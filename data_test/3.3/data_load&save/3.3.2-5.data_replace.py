import numpy as np
import pandas as pd

data = pd.Series([1,2,3,888,5,999])

print("Data is :\n",data)
print("Replace 999:\n", data.replace(999,'-1')) # 使用-1替换999

# 一次性替换多值
print("Replace 888 and 999:\n",data.replace([888,999],[0,-2]))