from flask import Flask, jsonify, request, render_template, redirect, url_for
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///database.sqlite')


@app.route('/')
def home_page():
	return render_template('home_page.html')

    
@app.route('/get_data', methods=['GET'])
def get_data():
    con = engine.connect()
    data = con.execute('SELECT value, timestamp FROM akingscote ORDER BY timestamp DESC limit 1')
    value, timestamp = data.first()

    con.close()

    print value, timestamp
    return jsonify(dict(value=value, timestamp=timestamp))
    

app.run(debug=True)