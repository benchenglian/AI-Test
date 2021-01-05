import os,re
import time

print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))

line = "关键\n词语\n测试\n名师"
print(re.sub("\n",",",line))

# 获取当前时间戳
now_time = time.time()
format_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(format_date)

# 秒级时间戳
date_time = 1574605194
format_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(date_time))
print(format_date)


