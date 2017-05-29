import os

from sqlalchemy import Integer, String, Float, DateTime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from time import sleep
import datetime
HOST = 'localhost'
PORT = 5000

DATABASE_NAME = 'database'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}.sqlite'.format(DATABASE_NAME)
database = os.path.join(os.path.dirname(__file__), SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)

class akingscote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Float(20))
	timestamp = db.Column(db.DateTime)


# Reset all the database tables
db.create_all()

if __name__ == '__main__':
    print 'adding some default data'
    time = datetime.datetime.utcnow()
    data = akingscote(timestamp=time, value=0.001)
    db.session.add(data)
    db.session.commit()
    print 'finished'