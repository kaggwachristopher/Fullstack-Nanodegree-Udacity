from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
   app.run(host="0.0.0.0")
