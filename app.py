from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)


@app.route('/')
def index():
	return "Pludy System"

@app.route('/jaehwan')
def jaehwan():
	return "사랑해"

@app.route('/yejin')
def yejin():
	return "사랑해22"

@app.route('/yejin2')
def yejin2():
	return "사랑해23"

@app.route('/yejin3')
def yejin3():
	return "사랑해233"

if __name__=="__main__":
	app.run()

class User(db.Model):
	__table_name__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False)
	schoolname = db.Column(db.String(120), nullable=False)
	grade = db.Column(db.Integer(), nullable=False)
	phonenumber = db.Column(db.String(100), unique=True)
	pphonenumber = db.Column(db.String(100), unique=True, nullable=False)

	def __repr__(self):
		return f"<User('{self.id}', '{self.username}', '{self.schoolname}','{self.grade}','{self.phonenumber}')>"
