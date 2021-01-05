import random,numpy
# 1.利用sum()函数求和
print(sum(range(0,101)))

# 2.利用global 修改全局变量
a = 5
def fn():
    global a
    a = 4
fn()
print(a)

# 列出5个python标准库
# os：提供了不少与操作系统相关联的函数
# sys:   通常用于命令行参数
# re:   正则匹配
# math: 数学运算
# datetime:处理日期时间

# 4、字典如何删除键和合并两个字典 del和update方法
dic = {"name":"zs","age":18}
del dic["name"]
print(dic)
dic2 = {"name":"1s"}
dic.update(dic2)
print(dic)

# 6、python实现列表去重的方法;先通过集合去重，在转列表
list = [11,12,13,12,15,16,13]


a = set(list)
print(a)
print([x for x in a])

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

# 8、python2和python3的range（100）的区别?答案：python2返回列表，python3返回迭代器，节约内存
# for i in range(100):
#     print(i)

# 9、一句话解释什么样的语言能够用装饰器? 答案：函数可以作为参数传递的语言，可以使用装饰器

# 10、python内建数据类型有哪些 ？
#整型--int
#布尔型--bool
#字符串--str
#列表--list
#元组--tuple
#字典--dict

'''
11）python提供的内置类型是什么？

有可变和不可变类型的Pythons，内置类型为Mutable内置类型
List
Sets
Dictionaries
不可变的内置类型
Strings
Tuples
Numbers
'''
print([i*i for i in range(0,101) if i % 2 == 0])

# def test_first():
#     print("Now test start...")
#     while True:
#         res = yield 4
#         print("res",res)
#
# rest_infor = test_first()
# print(next(rest_infor))
# print("*"*10)
# print(next(rest_infor))
# print(rest_infor.send(7))

# 9x9 乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
# 递归5的阶乘
def jc(n):
    if n == 1:
        return 1
    return n * jc(n-1)
print(jc(5))