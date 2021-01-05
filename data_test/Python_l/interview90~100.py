# 91、简述python引用计数机制
'''
python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。
引用计数算法。

当有1个变量保存了对象的引用时，此对象的引用计数就会加1

当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，即变为2，
当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''

# 92、int("1.4"),int(1.4)输出结果？
# int("1.4")报错，int(1.4)输出1

# 93、列举3条以上PEP8编码规范
import re

'''
1、顶级定义之间空两行，比如函数或者类定义。

2、方法定义、类定义与第一个方法之间，都应该空一行

3、三引号进行注释

4、使用Pycharm、Eclipse一般使用4个空格来缩进代码
'''

# 94、正则表达式匹配第一个URL indall结果无需加group(),search需要加group()提取
s = '<img data-v-0154e9e8="" src="https://cdn-creatives-qa.inmobi.cn/demand/demand-creatives/86/image/20201106/7db8ad96d0ec407bae9b99eac5e7adf3/94174447f7ba48a6aced5761b2e95dae.jpeg" class="image">'
res = re.findall("https://.*?\.jpeg",s)
print(res[0])
res = re.search("https://.*?\.jpeg",s)
print(res.group())

# 95、正则匹配中文
title = '你好,hello,世界'
patten = re.findall('[^a-zA-Z,]+',title)
print(patten)

# 96、简述乐观锁和悲观锁
"""
悲观锁, 就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。
传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。

乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，
可以使用版本号等机制，乐观锁适用于多读的应用类型，这样可以提高吞吐量
"""

# 97、r、r+、rb、rb+文件打开模式区别 https://www.cnblogs.com/liangliangzz/p/10318076.html

# 98、Linux命令重定向 > 和 >>
'''
> 表示输出，会覆盖文件原有的内容
< 使cmd命令从file读入
>> 表示追加，会将内容追加到已有文件的末尾
<< 从命令行读取输入，直到一个与text相同的行结束。除非使用引号把输入括起来，此模式将对输入内容进行shell变量替换。如果使用<<- ，
则会忽略接下来输入行首的tab，结束行也可以是一堆tab再加上一个与text相同的内容，可以参考後面的例子。

https://zhidao.baidu.com/question/196553141.html

https://blog.csdn.net/world_zheng/article/details/83110029
'''

# 99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
s = '<html><h1>www.itcast.cn</h1></html>'
#res = re.findall("^(<\w+>).*?[^<(/\w*)>]",s)
res = re.findall(r"<(\w+)><(\w+)>(.*)</\2></\1>",s)
#res = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>",s)
#print(res)
print(res[0][2])

# 100、python传参数是传值还是传址？
'''
Python中函数参数是引用传递（注意不是值传递）。对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；
而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
'''


