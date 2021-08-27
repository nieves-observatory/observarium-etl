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


class ExoplanetsModel(db.Model):
    __tablename__ = "exoplanets"
    id = db.Column(db.Integer, primary_key=True)
    planet = db.Column(db.String, unique=True, nullable=False)
    ra = db.Column(db.String, nullable=False)
    dec = db.Column(db.String, nullable=False)
    mag = db.Column(db.String, nullable=False)
    period = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    depth = db.Column(db.String, nullable=False)
    midpoint = db.Column(db.String, nullable=False)


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
f_contents = open('bright_transits.csv', 'r')

db_cursor.copy_from(f_contents, "exoplanets", columns=(
    "planet", 'ra', 'dec', 'mag', 'period', 'duration', 'depth', 'midpoint'), sep=",")
print("load complete")
db_conn.commit()

db_cursor.close()
db_conn.close()
print("connection closed")
