# 101、求两个列表的交集、差集、并集

a = [1,2,3,4]
b = [4,3,5,6]

jj1 = [i for i in a if i in b] # a中的i，并且在b中。交集。
jj2 = list(set(a).intersection(set(b)))

bj1 = list(set(a).union(set(b))) #并集
bj2 = list(set(a + b))

cj1 = list(set(b).difference(set(a))) # b中有而a中没有
cj2 = list(set(a).difference(set(b))) # a中有而b中没有
cj3 = [i for i in a if i not in b] # a中有而b中没有
cj4 = [i for i in b if i not in a]  #b中有而a中没有

print("交集1",jj1)
print("交集2",jj2)
print("并集1",bj1)
print("并集2",bj2)
print("差集1",cj1)
print("差集2",cj2)
print("差集3",cj3)
print("差集4",cj4)

# 102、生成0-100的随机数
import random
res1 = 100 * random.random()#随机小数
res2 = random.choice(range(0,101))#随机整数
res3 = random.randint(1,100) #随机整数
print(res1)
print(res2)
print(res3)

# 103、lambda匿名函数好处、
# 精简代码，lambda省去了定义函数，map省去了写for循环过程
a = ["苏州","中国","哈哈","","","日本","","","德国"]
res = list(map(lambda  x :"填充值" if x == "" else x,a))
print(res)

# 104、常见的网络传输协议 UDP、TCP、FTP、HTTP、SMTP等等

# 105、、单引号、双引号、三引号用法
'''
1、单引号和双引号没有什么区别，不过单引号不用按shift，打字稍微快一点。表示字符串的时候，单引号里面可以用双引号，而不用转义字符,反之亦然。

'She said:"Yes." ' or  "She said: 'Yes.' "

2、但是如果直接用单引号扩住单引号，则需要转义，像这样：

 ' She said:\'Yes.\' '

3、三引号可以直接书写多行，通常用于大段，大篇幅的字符串

"""

hello

world

"""
'''

# 106、python垃圾回收机制
'''
python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。
引用计数算法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1

当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，
即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''

# 107、HTTP请求中get和post区别
'''
1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；

2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，
而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，
但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。

3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，
请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。
'''

# 108、python中读取Excel文件的方法
'''
应用数据分析库pandas
import pandas
df = pd.read_excel("333.xlsx")
print(df)
'''

# 109、简述多线程、多进程
'''
进程：

1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立

2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

线程：

1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，
一个进程下的多个线程可以共享该进程的所有资源

2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃

应用：

IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间

CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，
当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势

'''

# 110、python正则中search和match
import re

s = "小明年龄18岁 工资10000"
res = re.search("\d+",s) # search匹配到第一个匹配到的数据
print("search结果",res)

res = re.findall("\d+",s) # 满足正则都匹配，不用加group
print(res)

res = re.match("小明",s).group() #  匹配以 小明 开头的字符串，并匹配出小明
print(res)

res = re.match("\d+",s)
print("试错，不加gourp为none，匹配不到",res) # 不加group匹配不到

res = re.match("工资",s).group() #工资不是字符串开头，匹配不到，报错
print(res)