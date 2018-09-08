#!/usr/bin/env python
import base64
import redis
import pymysql

class StoreDataInDataBase():
	# 声明一个静态方法
	@staticmethod
	def save_key_1_redis(key_name,member):
		# 连接Redis
		connection = redis.StrictRedis("127.0.0.1","6379")
		# 调用了sadd方法,向集合对象添加成员
		connection.sadd(key_name,member)
		print(connection.smembers("key"))

	@staticmethod
	def save_key_1_mysql(key_name,member):
		# 打开数据库连接
		db = pymysql.connect("localhost","root","123456","test")
		# 使用cursor()方法获取操作游标 
		cursor = db.cursor()
		# SQL 插入语句
		sql = "INSERT INTO TEST(ID) VALUES (member) "
		try:
			# 使用execute方法执行SQL语句
		    cursor.execute(sql)
		    # 提交到数据库执行
		    db.commit()
		except:
			# 发生错误时回滚
			db.rollback()
		# 关闭数据库连接
		db.close()


if __name__ == '__main__':
	for i in range(100,300):
		push_key = 'Apple Store App ' + str(i*(i-1))
		encode_push_key = base64.b64encode(push_key.encode('utf-8'))
		StoreDataInDataBase.save_key_1_redis(encode_push_key)
		StoreDataInDataBase.save_key_1_mysql(encode_push_key)
