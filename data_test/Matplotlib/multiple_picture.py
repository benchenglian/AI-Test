import numpy as np
import  matplotlib.pyplot as plt
figure,ax = plt.subplots()

# 图表总标题
figure.suptitle('subplots demo')

# 第一个子图———误差线图
x = np.linspace(0,10,50)
data1 = np.sin(x) + x*0.7
plt.subplot(2,2,1)
plt.errorbar(x,data1,yerr=x*0.7,fmt='.k',ecolor='blue')

# 第二个子图———饼图
data2 = [0.1,0.2,0.3,0.15,0.25]
plt.subplot(2,2,2)
plt.pie(data2)

# 第三哥子图————等高线
# 构造数据，计算x、y坐标对应的高度值
def f(x,y):
    return np.sin(x) ** 10 + np.cos(x*y+10) * np.cos(x)

x = np.linspace(0,5,50) # 生成xy数据
y = np.linspace(0,5,40)
x,y = np.meshgrid(x,y) # 得到网格点矩阵

plt.subplot(2,2,3)
plt.contour(x,y,f(x,y),colors = 'green')

# 第四个子图———直方图
data4 = np.random.randn(1000)
plt.subplot(2,2,4)
plt.hist(data4)

plt.show()