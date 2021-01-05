# 合并数据集
import pandas as pd
import numpy as np
df1 = pd.DataFrame({'id':[1,2,3,4],'val1':['a','b','a','a']})
df2 = pd.DataFrame({'id':[1,2,3],'val2':['b','c','d']})
print("df1 is :\n",df1)
print("df2 is :\n",df2)
print("merge:\n",pd.merge(df1,df2,on='id'))