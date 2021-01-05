# 处理重复数据
import pandas as pd

data = pd.DataFrame({"A":['a','b']*3 + ['a','b'],"B":[1,1,2,2,3,3,2,3]})
print("Data is :\n",data)
print("数据是否重复 : \n ",data.duplicated())
print("A列数据是否重复 : \n ",data.duplicated(['A']))


# 删除重复数据
print('删除重复数据:\n',data.drop_duplicates()) # 删除重复行
print('删除A列的重复数据\n',data.drop_duplicates(['A'])) # 删除A列的重复数据