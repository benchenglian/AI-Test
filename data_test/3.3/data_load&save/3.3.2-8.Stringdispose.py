#字符串处理，通常使用Python 内置的字符串处理方法

text = 'a, b,c,    d,    test'
splittext = text.split(',') # 字符串分割
striptext = [x.strip() for x in splittext] # 去除分割后字符串中的空格
print('split:',splittext)
print('strip:',striptext)

print('join:',"~".join(striptext)) # 字符串拼接

print('find:', text.find('c')) # 字符串查找

print('replace', text.replace('t','o')) #字符串替换

import re
# 借助正则表达式，完成复杂的字符串匹配、替换和拆分
text = 'test a\t tb\n test b'
#print('text',text)
print('re.split:\n',re.split('\s+',text)) # 使用1哥或多个空白符拆分字符串

regex = re.compile('\s+')

print('use regex:\n',regex.split((text))) # 使用compile编译regex对象

print('findall:\n',regex.findall(text)) # findall得到匹配的模式

print('search:\n',regex.search(text)) # search返回第一哥匹配到的对象，包含起止位置

print('match:\n',regex.match(text)) # 从字符串起始位置开始匹配，匹配成功就返回匹配的对象，否则返回None

print('sub:\n',regex.sub('~',text)) # sub函数可以将匹配到的内容进行替换

