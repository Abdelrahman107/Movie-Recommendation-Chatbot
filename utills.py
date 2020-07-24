from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FourBots.db'
app.config['SECRET_KEY'] = 'Four1234'

db=SQLAlchemy(app)

class User(db.Model):
    age=db.Column(db.Integer,nullable=False)
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.age}')"

test=User.__repr__(self)
print(test)