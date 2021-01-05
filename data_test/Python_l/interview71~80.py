# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
list_a=[0,-1,3,-10,5,9]
list_a.sort(reverse=False)
print("list.sort在list基础上修改，无返回值",list_a)

list_b=[0,-1,3,-10,5,9]
res = sorted(list_b,reverse=False)
print("sorted有返回值是新的list",list_b)
print("返回值",res)

# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:x)
print(a)

# 73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# a = sorted(foo)[::-1]
a = sorted(foo,key=lambda x:(x<0,abs(x)))
print(a)

# 74、列表嵌套字典的排序，分别根据年龄和姓名排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54},
        {"name":"wa","age":17},{"name":"df","age":23}]

b = sorted(foo,key = lambda x:x["age"],reverse=True) # 按年龄从大到小
print(b)
c = sorted(b,key = lambda x:x["name"]) # 姓名从小到大。
print(c)

# 75、列表嵌套元组，分别按字母和数字排序
foo = [("zs",19),("ll",54),
       ("wa",17),("df",23)]
a = sorted(foo,key=lambda x:x[0])# 按字母从小到大
print(a)
a = sorted(foo,key=lambda x:x[1],reverse=True)# 按数字从大到小
print(a)

# 76、列表嵌套列表排序，年龄数字相同怎么办？
foo = [["zs",19],["ll",54],
       ["wa",23],["df",23],["xf",23]]
a = sorted(foo,key=lambda x:(x[1],x[0])) # 年龄相同按字母排序。
print(a)
a = sorted(foo,key=lambda x:x[0])
print(a)

# 77、根据键对字典排序（方法一，zip函数）
dic = {"name":"zs","sex":"man","city":"bj"}
foo = zip(dic.keys(),dic.values()) # 字典转换嵌套元组
foo = [i for i in foo]
print("字典转换成嵌套元组",foo)
b = sorted(foo,key=lambda x:x[0])# 字典嵌套元组排序
print("根据键排序",b)
new_dic = {i[0]:i[1] for i in b}
print("字典推导式构造新字典",new_dic)

# 78、根据键对字典排序（方法二,不用zip)
dic = {"name":"zs","sex":"man","city":"bj"}
print(dic.items())
b = sorted(dic.items(),key=lambda x:x[0])
print("根据键排序",b)
new_dic = {i[0]:i[1] for i in b}
print("字典推导式构造新字典",new_dic)

# 79、列表推导式、字典推导式、生成器
import random
td_list = [i for i in range(10)]
print("列表推导式",td_list,type(td_list))

ge_list = (i for i in range(10))
print("生成器",ge_list)

dic = {k:random.randint(4,9) for k in ['a','b','c','d']}
print("字典推导式",dic,type(dic))

# 80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
s = ["ab","abc","a","adkj"]
a = sorted(s,key=lambda x:len(x))
print(a)