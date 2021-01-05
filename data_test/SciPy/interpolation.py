# 插值运算

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,10,num=11,endpoint=True)
y = np.cos(-x**2/9.0)

f1 = interp1d(x,y,kind='linear')
f2 = interp1d(x,y,kind='cubic')

xnew = np.linspace(0,10,num=41,endpoint=True)

plt.plot(x,y,'o',xnew,f1(xnew),'-',xnew,f2(xnew),'--')
plt.legend(['data','linear','cubic'],loc='best')
plt.show()