# 31两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
import datetime

list1 = [1,5,7,9]
list2 = [2,2,6,8]
list1.extend(list2)
print(list1)
list1.sort(reverse=False)
print(list1)

# 32用python删除文件和用linux命令删除文件方法
# python os.remove(文件名)
# rm 文件名

# 33.log日志中，我们需要用时间戳记录error，warning等的发生时间，请用datetime模块打印当前时间戳"2018-04-01 11:38:54"
# 顺便把星期的代码
print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) +' 星期: ' + str(datetime.datetime.now().isoweekday()))

# 34.数据库优化查询的方法
# 外键、索引、联合查询、选择特定字段等等。

# 35.列出你会的任意一种统计图(条形图、折线图等)绘制的开源库，第三方也行。
# pychart、matplotlib



# 36.写一段自定义一场代码 自定义异常用raise抛出异常
# 用raise自定义异常
def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)
fn()

'''
37、正则表达式匹配中，（.*）和（.*?）匹配区别？
（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
'''
s = "<a>哈哈</a><a>呵呵</a>"
import re
res1 = re.findall("<a>(.*)</a>",s)
print('贪婪匹配',res1)
res2 = re.findall("<a>(.*?)</a>",s)
print('非贪婪匹配',res2)

'''
38、简述Django的orm

ORM，全拼Object-Relation Mapping，意为对象-关系映射

实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，
而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，
翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，
如果数据库迁移，只需要更换Django的数据库引擎即可
'''
#39.[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
# 使用列表推导式
print([j for i in [[1,2],[3,4],[5,6]]for j in i] )
# 使用numpy矩阵，通过numpy的faltten()方法；
import numpy as np
b = np.array([[1,2],[3,4],[5,6]]).flatten().tolist()
print(b)

# 40.x = "abc",y = "def",z = ["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

x = "abc"
y = "def"
z = ["d","e","f"]
m = x.join(y)
n = x.join(z)
print(m)
print(n)
