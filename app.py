from flask import Flask, request, jsonify
from database import db
from models.meals import Meal


app = Flask(__name__)

#Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db.init_app(app)

if __name__ == '__main__':
  app.run(debug=True)