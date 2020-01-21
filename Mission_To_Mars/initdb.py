# from app import mongo

from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import pymongo 

# db.drop_all()

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
# Use PyMongo to establish Mongo connection

# working for FLASK_APP
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# working for Heroku
conn = 'mongodb://username:password@ds055545.mlab.com:55545/heroku_f78hk1fg'
mongo = pymongo.MongoClient(conn, port=port)


