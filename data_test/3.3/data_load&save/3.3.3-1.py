# 层次化索引
import pandas as pd
import numpy as np
data = pd.Series(np.random.randn(6),index= [
    ['a','a','b','b','c','c'],
    [1,2,1,2,1,2]
])
print("data is :\n",data)
print("data.index: \n",data.index)

print("data['b']:\n",data['b'])

print("data['b':'c']:\n",data['b':'c'])

print("data.loc[:2]:\n",data.loc[:,2])

# unstarck()
print("data.unstack():\n",data.unstack())
print("data.unstack():\n",data.unstack().stack())

# DataFrame结构的数据也可以有层次化索引。
df = pd.DataFrame(np.arange(12).reshape((4,3)),
                  index=[
                      ['a', 'a', 'b', 'b'],
                      [1, 2, 1, 2]],
                  columns= [['A','A','B'],
                            [1,2,1]
                  ])
print("df is :\n",df)
print("df[A] is :\n",df['A'])

df.index.names = ['k1','k2'] # 为每层添加索引。
df.columns.names = ['char','num'] # 为每列添加索引。
print("df is :\n",df)

print("Use swaplevel:\n",df.swaplevel('k1','k2')) # 调整各级别的顺序
print("Use sort_index:\n",df.sort_index(level=1)) # 按照指定的级别索引进行排序

print("sum by level :\n",df.sum(level='k1')) # 根据级别进行数据的汇总统计