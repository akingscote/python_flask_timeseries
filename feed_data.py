import datetime
import random
from flask import Flask
from sqlalchemy import create_engine
from time import sleep

engine = create_engine('sqlite:///database.sqlite')
con = engine.connect()
while True:
    try:
        time=datetime.datetime.utcnow()
        data = random.uniform(0,100)
        con.execute("INSERT INTO akingscote (value, timestamp) VALUES ({}, '{}')".format(data, time))
        print 'Inserted {}, {}'.format(data, time)
        sleep(1)

        
    except KeyboardInterrupt:
        con.close()

con.close()