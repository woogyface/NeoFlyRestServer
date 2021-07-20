from flask import Flask, request, jsonify
from NFDB import nfdb

dbfile = "C:/ProgramData/NeoFly/common.db"
db = nfdb()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return "Hello, World!"

@app.route('/query/<string:sql>', methods=['GET'])
def query(sql):
	con = db.connect(dbfile)
	data = db.query(con, sql)
	db.diconnect(con)
	return jsonify(data)
	
@app.route('/tables', methods=['GET'])
def tables():
	con = db.connect(dbfile)
	data = db.tables(con)
	db.diconnect(con)
	return jsonify(data)
	
@app.route('/tables/<string:table_name>', methods=['GET'])
def header(table_name):
	con = db.connect(dbfile)
	data = db.header(con, table_name)
	db.diconnect(con)
	return jsonify(data)

if __name__ == "__main__":
	app.run(debug=True)