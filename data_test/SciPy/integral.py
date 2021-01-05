# 数值积分
# 求解单位圆的面积 , x^2 + y^2 = 1
import numpy as np
from scipy import integrate
# 半圆的面积可以看作y的积分，y=(1-x^2)^0.5
def half_circle(x):
    return (1-x**2) ** 0.5

pi_half , err = integrate.quad(half_circle,-1,1)
# 从 -1 到 1 进行积分，得到半圆的面积，err是误差
print("pi_half:",pi_half,"err",err)
# pi_half: 1.5707963267948983 err 1.0002354500215915e-09

print("2*pi_half:",2*pi_half)
# 2*pi_half: 3.1415926535897967

# 求解单位球的体积
def half_sphere(x,y):
    return (1-x**2-y**2)**0.5

half_sphere,err = integrate.dblquad(half_sphere,-1,1,
                                    lambda x: -half_circle(x),
                                    lambda x: half_circle(x)
                                    )
print("2*half_sphere:",2*half_sphere)
#2*half_sphere: 4.188790204786397
