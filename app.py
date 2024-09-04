from flask import Flask, render_template, request
import sqlalchemy as db
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine("sqlite:///demo.db")
session = Session(engine)

Base = declarative_base()
class HuntUser(Base):
    __tablename__ = 'huntuser'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

Base.metadata.create_all(engine)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    print(request.args['huntname'], flush=True)
    u = HuntUser(name=request.args['huntname'])
    session.add(u)
    session.commit()
    users = session.query(HuntUser).all()
    return str(users)

@app.get("/user")
def user():
    return render_template("user.html")

def init():
    connection = engine.connect()

if __name__ == '__main__':
    print("running...")
    init()
    app.run(host='0.0.0.0', port=80, debug=False)