from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
   app.run(host="0.0.0.0")
