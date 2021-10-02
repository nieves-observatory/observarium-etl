from flask import Flask  # to render the error page
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost/dso_without_errors"
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


db_conn = psycopg2.connect(host="localhost", port="5432",
                           dbname="dso_without_errors", user="postgres")
db_cursor = db_conn.cursor()
print("connection success")
f_contents = open('dso_complete.csv', 'r')

db_cursor.copy_from(f_contents, "dso", columns=("params", 'name', 'ngcic', 'common', 'type', 'ra', 'dec', 'mag', 'dist', 'con',
                                                'image'), sep=",")
print("load complete")
db_conn.commit()

db_cursor.close()
db_conn.close()
print("connection closed")
