from flask import Flask, request, jsonify, url_for, make_response
from NFDB import nfdb

dbfile = "C:/ProgramData/NeoFly/common.db"
db = nfdb()
app = Flask(__name__)


def has_no_empty_params(rule):
	defaults = rule.defaults if rule.defaults is not None else ()
	arguments = rule.arguments if rule.arguments is not None else ()
	return len(defaults) >= len(arguments)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['GET'])
def home():
	return site_map()

@app.route("/site-map", methods=['GET'])
def site_map():
	links = []
	for rule in app.url_map.iter_rules():
		if "GET" in rule.methods and has_no_empty_params(rule):
			url = url_for(rule.endpoint, **(rule.defaults or {}))
			links.append(url)

	response = jsonify(links)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/query/<string:sql>', methods=['GET'])
def query(sql):
	con = db.connect(dbfile)
	data = db.query(con, sql)
	db.diconnect(con)
	response = jsonify(data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response
	
@app.route('/tables', methods=['GET'])
def tables():
	con = db.connect(dbfile)
	data = db.tables(con)
	db.diconnect(con)
	response = jsonify(data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response
	
@app.route('/tables/<string:table_name>', methods=['GET'])
def header(table_name):
	con = db.connect(dbfile)
	data = db.header(con, table_name)
	db.diconnect(con)
	response = jsonify(data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__ == "__main__":
	app.run(debug=True)