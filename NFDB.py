import sqlite3 as sql
from sqlite3 import Error

class nfdb():
	def connect(self, file):
		conn = None
		try:
			conn = sql.connect(file)
			print(sql.version)
			return conn
		except Error as e:
			print(e)

	def diconnect(self, connection):
		if (connection):
			connection.close()

	def query(self, connection, sql):
		cursor = connection.cursor()
		cursor.execute(sql)

		rows = cursor.fetchall()
		for row in rows:
			print(row)

		return rows