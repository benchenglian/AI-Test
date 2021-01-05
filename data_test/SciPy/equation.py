import numpy as np
from scipy import linalg

# 2x - y = 0
# x + 3y = 7
a = np.array([[2,-1],
              [1,3]])
b = np.array([0,7])

# 求解方程组
x,y = linalg.solve(a,b)
print("x=",x,"y=",y) # x= 1.0 y= 2.0