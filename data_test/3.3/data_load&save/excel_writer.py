import pandas as pd
import numpy as np
# 2.Excel电子表格-2

df1 = pd.DataFrame(np.array([[1,2],[3,1],[5,6],[7,2]]),columns=['A','B'])
df2 = pd.DataFrame(np.array([[1,2],[3,4],[5,6]]),columns=['A','B'])

# 创建一个空的excel
excel = pd.DataFrame()
excel.to_excel('data1.xlsx')

#打开Excel文件，写入数据
writer = pd.ExcelWriter('data1.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')

#保存writer中的数据至excel文件中
writer.save()