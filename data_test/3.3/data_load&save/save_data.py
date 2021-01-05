import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[1,2],[3,1],[5,6],[7,2]]),columns=['A','B'])
df.to_csv('savedata.csv','|') #写入csv文件