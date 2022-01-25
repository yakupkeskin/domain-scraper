from flask import Flask,render_template
from database import Database


app = Flask(__name__)

@app.route('/')
def homes():
	return render_template('home.html')
@app.route('/whois')
def whois():
	db = Database()
	rows = db.select_from_whois()
	return render_template('whois.html',content=rows)
@app.route('/domains')
def domains():
	db = Database()
	rows = db.select_from_subdomains()
	return render_template('domain.html',content = rows)

if __name__ == '__main__':
	app.run(debug = True)
