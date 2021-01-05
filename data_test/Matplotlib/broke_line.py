# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)
z = np.cos(x)
plt.style.use('seaborn-whitegrid') # 设置图像显示风格
fig = plt.figure(figsize=(8,4)) # 创建图，并指定大小

plt.rcParams['font.family'] = ['Arial Unicode MS'] # 设置字体
plt.title('sin(x) and cos(x)') # 设置图片的标题
plt.xlabel('x轴') # 设置x轴的标题
plt.ylabel('y轴') # 设置y轴的标题
plt.xlim(-2.5,12.5) # 设置x轴的上下限
plt.ylim(-2,3) # 设置y轴的上下限

# 作图，可以指定线条颜色、样式(实线、虚线等)、图例等
sin_line = plt.plot(x,y, label = '$\sin(x)$', color='red', linestyle = 'dashdot')
cos_line = plt.plot(x,z, label = '$\cos(x)$', color=(0.2,0.8,0.3), linestyle = '--')
plt.plot(x,y+1,':c',label = '$\sin(x)+1$')

# 展示图例，设置展示位置、样式、要展示的图片内容等
plt.legend(loc='upper left',frameon=True)
plt.show()
