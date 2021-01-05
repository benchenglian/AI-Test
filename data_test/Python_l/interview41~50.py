'''
41.举例说明异常模块try except else finally的相关意义
try...except...else没有捕获异常，执行else语句
try...except...finally不管是否捕获异常，都执行finally语句
'''
import re

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，则执行该语句')


try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
finally:
    print('不管是否捕获到异常，则执行该语句')

# 42.python中交换连个数值
a,b = 3,4
print(a,b)
a,b = b,a
print(a,b)

'''
43.举例说明zip()函数方法
zip()函数在运算时，会以一个或多个序列(可迭代对象)作为参数，返回一个元组的列表，同时将这些序列中并排的元组配对。
zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数；当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。
'''
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print(res)
a = (1,2)
b = (3,4)
res = [i for i in zip(a,b)]
print(res)
a = "ab"
b = "xyz"
res = [i for i in zip(a,b)]
print(res)

# 44.a = "张明 98分"，用re.sub，将98转成100
a = "张明 98分"
print(re.sub('\d+',"100",a))

'''
45、写5条常用sql语句

show databases;

show tables;

desc 表名;

select * from 表名;

delete from 表名 where id=5;

update students set gender=0,hometown="北京" where id=5
'''

#46、a="hello"和b="你好"编码成bytes类型
a=b"hello"
b="你好".encode()
print(a,b)
print(type(a),type(b))

# 47.[1,2,3]+[4,5,6]等于多少？ 两个列表相加，等价于extend
a=[1,2,3]
b= [4,5,6]
res=a+b
print(res)
result = map(lambda x,y:x+y,a,b)
print(list(result))

'''
48、提高python运行效率的方法

1、使用生成器，因为可以节约大量内存

2、循环代码优化，避免过多重复代码的执行

3、核心模块用Cython  PyPy等，提高效率

4、多进程、多线程、协程

5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
'''

'''
49、简述mysql和redis区别

redis： 内存型非关系数据库，数据保存在内存中，速度快

mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢
'''

'''
50、遇到bug如何处理

1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log

2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。

3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。

4、导包问题、城市定位多音字造成的显示错误问题
'''