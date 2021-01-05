import pandas as pd
data = pd.read_csv('ex1.csv')
print("read_csv :\n",data)

data = pd.read_csv('ex1.csv', skiprows=[2]) # 跳过指定列
print("\nread_table whith skiprows :\n",data)

data = pd.read_table('ex1.csv', sep=',') #指定分隔符
print("\nread_table :\n",data)

data = pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd'], index_col='a')
print("data_switch is : \n",data)

data = pd.read_csv('ex3.csv') # NaN
print("data is : \n",data)