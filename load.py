from flask import Flask  # to render the error page
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
db = SQLAlchemy(app)


class DSOModel(db.Model):
    __tablename__ = "dso"
    id = db.Column(db.Integer, primary_key=True)
    params = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    ngcic = db.Column(db.String, nullable=False)
    common = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    ra = db.Column(db.String, nullable=False)
    dec = db.Column(db.String, nullable=False)
    mag = db.Column(db.String, nullable=False)
    dist = db.Column(db.String, nullable=False)
    con = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)


db.create_all()
print("create model success")


t_host = os.getenv("t_host ")
t_port = os.getenv("t_port")
t_dbname = os.getenv("t_dbname")
t_user = os.getenv("t_user")
t_pw = os.getenv("t_pw")
db_conn = psycopg2.connect(host=t_host, port=t_port,
                           dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()
print("connection success")
f_contents = open('complete_messier.csv', 'r')

db_cursor.copy_from(f_contents, "dso", columns=("params", 'name', 'ngcic', 'common', 'type', 'ra', 'dec', 'mag', 'dist', 'con',
                                                'image'), sep=",")
print("load complete")
db_conn.commit()

db_cursor.close()
db_conn.close()
print("connection closed")
