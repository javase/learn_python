# -*- coding: utf-8 -*-
# 导入MySQL驱动
import mysql.connector
# 注意把passport设为你的root口令
conn = mysql.connector.connect(host='10.1.64.80',port='9035',user='healthcloud',password='healthcloud123456',database='vaccine_server_core')
cursor = conn.cursor()
# 执行查询
cursor.execute("select version()")
# 使用fetchone()方法获取点条数据
data = cursor.fetchone()
print("Database version:%s" %data)

# 查询表数据
user_sql = 'select id,nickname,mobile from tb_account_user t'
cursor.execute(user_sql)
for id,nickname,mobile in cursor:
	print(id,nickname,mobile)
# 关闭数据库连接
conn.close()