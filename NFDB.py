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

	def fetchall(self, connection, sql):
		cursor = connection.cursor()
		cursor.execute(sql)

		rows = cursor.fetchall()
		return rows

	def query(self, connection, sql):
		return self.fetchall(connection, sql)

	def tables(self, connection):
		return self.fetchall(connection, "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")

	def header(self, connection, table):
		return self.fetchall(connection, "SELECT name FROM PRAGMA_TABLE_INFO('"+table+"');")
