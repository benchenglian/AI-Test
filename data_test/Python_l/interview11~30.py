# 21、列出python中可变数据类型和不可变数据类型，并简述原理
"""
不可变数据类型：数值型、字符串型String和元组tuple
不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则值有一个对象（一个地址）
"""
import re

a = 3
b = 3
print(id(a))
print(id(b))

"""
可变数据类型：列表list和字典dict；
允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，
变量引用的对象的地址也不会变化，不过对于相同的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当与内存中对于同值的对象保存了多份，
这里不存在引用计数，是实实在在的对象。
"""
a =[1,2]
b = [1,2]
print(id(a))
print(id(b))

# 22. s= "ajldjlajfdljfddd",去重并从小到大排序输出"adfjl"
s= "ajldjlajfdljfddd"
s = set(s)
n = list(s)
n.sort(reverse=False)
res = "".join(n)
print(type(res),res)


# 23.用lambda函数实现两个数相乘
sum = lambda a,b:a*b
print(sum(5,4))

# 24.字典根据键从小到大排序
dict = {"name":"zs","age":18,"city":"深圳","tel":1362626627}
list_a = sorted(dict.items(),key=lambda i:i[0],reverse=False)
print("sorted根据字典键排序",list_a)
new_dict={}
for i in list_a:
    new_dict[i[0]]=i[1]
print("新字典",new_dict)

# 25.利用collections库的counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

# 26.字符串 a = "not 404 found 张三 99 深圳"，每个单词中间是空格，用正则过滤掉英文和数组，最终输出张三。
a = "not 404 found 5.5 张三 99 深圳"

#list_b = a.split(" ")
res1 = re.findall("[^\d+\.?\d*a-zA-Z\s]+",a)
print(res1)
new_str= " ".join(res1)
print(new_str)
# for i in res1:
#     if i in list_b:
#         list_b.remove(i)
# print(list_b)
# new_str= " ".join(list_b)
# print(new_str)

# 27.filter方法求出列表所有奇数并构造列表, a = [1,2,3,4,5,6,7,8,9,10]
a = [1,2,3,4,5,6,7,8,9,10]
def fn(a):
    return a%2 == 1
newlist = filter(fn,a)
newlist = [i for i in newlist]
print(newlist)

# 28.列表推导式求列表所有奇数并构造新列表，a = [1,2,3,4,5,6,7,8,9,10]
res = [i for i in a if i%2==1]
print(res)

# 29.正则re.complie作用
# re.complie是将正则表达式变异成一个对象，加快速度，并重复使用

# 30.a=(1,) b=(1),c=("1")分别是什么类型的数据？
print(type((1,)))
print(type((1)))
print(type(("1")))

