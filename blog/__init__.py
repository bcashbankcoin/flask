from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL, MySQLdb
from flask_mail import Mail, Message
from flask_mail import Message
from flask_sqlalchemy import SQLAlchemy
import os

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
bcrypt = Bcrypt(app)
Bootstrap(app)

app.config['MAIL_SERVER'] = 'mail.bestsolution.me'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'demo@bestsolution.me'
app.config['MAIL_PASSWORD'] = '}ayWU]}e8Q)N'

mail = Mail(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '11111'
app.config['MYSQL_DB'] = 'flaskblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
MySQLdb = MySQLdb
mysql = MySQL(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskblog'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'static/images'


from blog import routes
