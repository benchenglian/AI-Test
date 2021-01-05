import random,numpy,re
# 11、简述面向对象中__new__和__init__区别
class Bike():
    # __init__方法自动调用，可以创建参数。
    def __init__(self,newWhellNum,newColor):
        self.whellNum = newWhellNum
        self.color = newColor

    def move(self):
        print("车会跑")

# 创建对象
BM = Bike(3,'green')
print('车的颜色为:%s'%BM.color)
print('车的数量为:%s'%BM.whellNum)

class A(object):
    def __init__(self):
        print("这是init方法",self)
        #__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，
        # __init__不需要返回值

    def __new__(cls): #__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
        print("这是cls的ID",id(cls))
        print("这是 new 方法",object.__new__(cls))
        return object.__new__(cls)
        #__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
        # 可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例

A()
print("这是类A的ID",id(A))
# 如果__new__创建的是当前类的实例，会自动调用__init__函数，
# 通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；
# 那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

# 12、简述with方法打开处理文件帮我我们做了什么？
with open("./1.txt","w") as f:
    f.write("hhh")
# 打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open写法，
# 我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，
# 都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close


#13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
#map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求


list = [1,2,3,4,5]
def fn(x):
    return x**2
res=map(fn,list)
res = [i for i in res if i>10]
print(res)

#14、python中生成随机整数、随机小数、0--1之间小数方法
print(random.randint(0,100))
print(numpy.random.randn(5))
print(numpy.random.randint(0,100,5))
print(round(random.random(),2))# 保留两位小数

# 15避免转义给字符串加哪个字母表示原始字符串？
# r , 表示需要原始字符串，不转义特殊字符


# 16 <div class = "nam">中国</div>,用正则匹配出标签里面的内容("中国")，其中class类名是不正确的
str = '<div class = "nam">中国</div>'
# res= re.search('<.*?>(.*?)</div>',str)
# print(res.group(1))
res2= re.sub('中国','中华',str)
print(res2)

#17 python中断言方法举例
a = 3
assert (a>1)
print("断言成功，程序继续向下执行")

b = 4
assert (b>7)
print("断言失败，程序报错")

# 18.数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct name from student

# 19.10个Linux常用命令
# ls pwd cd touch rm mkdir tree cp mv cat more grep echo

# 20.python2和python3区别？列举5个
# 1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi'),Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
# 2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# 3、python2中使用ascii编码，python中使用utf-8编码
# 4、python2中unicode表示字符串序列，str表示字节序列； python3中str表示字符串序列，byte表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要
# 6、python2中是raw_input()函数，python3中是input()函数