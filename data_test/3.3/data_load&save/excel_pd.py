import pandas as pd
# 2.Excel电子表格-1
# 通过创建excelfile类实例的方式，读取excel文件
xlsx = pd.ExcelFile('/Users/frank.lian/PycharmProjects/AI-Test/data_test/3.3/data_load&save/data.xlsx')
data = pd.read_excel(xlsx,'Sheet1')
print("data_switch is : \n" ,data)

# 直接读取excel文件
data = pd.read_excel('/Users/frank.lian/PycharmProjects/AI-Test/data_test/3.3/data_load&save/data.xlsx','Sheet1')
print("data_switch is :\n",data)