# chellamal_chai_shop

Install pip:
------------
sudo easy_install pip

pip -upgrade
-------------
sudo pip install --upgrade pip

Install - virutal env
----------------------
pip install virutalenv

create virutal environment
---------------------------
virutalenv flaskenv -p python3.0

Active virutalenv:
------------------
flaskenv bin/activate

Install Flask:
--------------
pip install Flask

Python shell : To view URL maps
--------------------------------
from Hello(filename) import app
app.url_map 

It Give the url (Routes) list in the app


WTForm:
------
pip install flask-wtf
pip install email_validator

MYSql:
-----
pip install SQLAlchemy
pip install Flask-SQLAlchemy

export PATH=$PATH:/usr/local/mysql/bin
pip install flask-mysqldb





Database:
---------
create database sample;
use  sample;
CREATE TABLE users ( username VARCHAR(30) NOT NULL,  mail VARCHAR(30) NOT NULL, password varchar(30) not null);

Generating securet key:
-----------------------
import os
os.urandom(8)

b'-P\x87e\x96Y\xbf|'


Generate database:
------------------

#from Hello import User
from flask_package.models import User
user_regular = User(username = 'shan',email='shan@gmail.com',password='shan@123')
db.session.add(user)
user_admin = User(username='admin',email='admin@gmail.com',password='admin@123')
db.session.add(user_admin)
db.session.commit()


User.query.all()
User.query.first()
User.query.filter_by(username='shan').all()

user_list = User.query.filter_by(username='shan').first()
User.query.get(2) # Here 2 is the Id (Primary key)
#Remove all data
db.drop_all()

Store password in database:
---------------------------
pip install flask-bcrypt


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

bcrypt.generate_password_hash('shan')
b'$2b$12$3mpGv6Azmv5EHYAQG7/juOsSYnPrsn0fEOie666Ilck9/lGuATP2K'

bcrypt.generate_password_hash('shan').decode('utf-8')
'$2b$12$bALN7V2JAYzueu0VYmWcT.asi7uKye.N.Rm5AtP96Eb8ib7K9qLAK'

hash_pw = bcrypt.generate_password_hash('shan').decode('utf-8')

bcrypt.check_password_hash(has_pw,'shan1')
False

bcrypt.check_password_hash(has_pw,'shan')
True

User session management:
------------------------
Pip install flask-login
