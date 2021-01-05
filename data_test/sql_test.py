import pymysql.cursors


# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='111111', db='customer',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = "SELECT * FROM user"
print(cursor.execute(sql))
result = cursor.fetchall()
print(result)
for data in result:
    print(data['name'])
connection.commit()
connection.close()

