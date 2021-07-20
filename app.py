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

if __name__ == "__main__":
	app.run(debug=True)