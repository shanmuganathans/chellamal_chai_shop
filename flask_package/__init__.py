
from flask import Flask
from logging import DEBUG
#password hash_key
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

#User session management
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = b'-P\x87e\x96Y\xbf|'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.logger.setLevel(DEBUG)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_package import routes