# 81、举例说明SQL注入和解决办法
import re

input_name = "zs"
sql = 'select * from demo where name = %s' % input_name
print("正常SQL语句",sql)

input_name = "zs;drop datebase demo"
sql = 'select * from demo where name = %s' % input_name
print("SQL注入语句",sql)
# 解决方式：通过传参数方式解决SQL注入
'''
params = [input_name]
count = cs.excute('select * from demo where name = %s',params)
原理：
Python的MySQLdb经过层层封装，各种调用，最后调用了mysql.h的mysql_real_escape_string()和mysql_escape_string()
这两个C API接口实现了对特殊字符的转义，从而起到了防止sql注入的作用。这个mysql.h头文件是在安装mysql时自带的，mysql官方出品，
对安全性有保证，同时也不用担心转义的字符不会被mysql识别从而引发一些问题。
同时经过这次源码剖析，也得出一个结论。无论使用什么语言对mysql进行操作，最终一定要调用mysql官方的mysql_real_escape_string()
接口(这个函数不光有C的API，市面上各大主流语言API该函数都有)，这样就可以应用官方提供的防注入处理函数来防止sql注入的发生。
更重要的是，一定要注意使用execute(query_str, (query_tuple))的方式对mysql进行操作，而不是execute("自行拼接的sql语句")，
否则无论第三方库封装地再好，都救不了你。
'''

# 82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
s="info:xiaoZhang 33 shandong"
res = re.split(":| ",s)
print(res)

# 83、正则匹配以163.com结尾的邮箱
email_list = ["xiaowang@163.com","xiaowang@163.comheihei",".com.xiaowang@qq.com"]
# for i in range(len(email_list)):
#     ret = re.search("\w+@163\.com$",email_list[i])
#     if ret:
#         print(ret.group())
#     else:
#         print(email_list[i])
for email in email_list:
    ret = re.search("\w+@163\.com$",email)
    if ret:
        print(ret.group())
    else:
        print(email)

# 84、递归求和,完成1+2+3+4....+10计算
def sum_test(num):
    if num>=1:
        res = num + sum_test(num-1)
    else:
        res = 0
    return res

print(sum_test(10))


# 85、python字典和json字符串相互转化方法
# json.dumps()字典转json字符串，json.loads()json转字典

'''
86、MyISAM 与 InnoDB 区别：
1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM就不可以了；

2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到安全性较高的应用；

3、InnoDB 支持外键，MyISAM 不支持；

4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM表中可以和其他字段一起建立联合索引；

5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；
'''
# 87、统计字符串中某字符出现次数
str = "张三 美国 张三 哈哈 张 三"
res = str.count("张三")
print(res)

# 88、字符串转化大小写
str = "HHHuuu"
print("upper",str.upper())#大写
print("lower",str.lower())#小写

# 89、用两种方法去空格
str = "hello world ha ha"
res = str.replace(" ","")
print(res)

ret = str.split()
s_ret = "".join(ret)
print(s_ret)

# 90、正则匹配不是以4和7结尾的手机号
tels = ["13100001234","18912344321","10086","188000007777"]
for tel in tels:
    ret = re.search("\d+4$|\d+7$",tel)
    if ret:
        print("以4和7结尾的手机号",ret.group())
    else:
        print("非4和7结尾",tel)