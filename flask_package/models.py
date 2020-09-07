
from flask_package import db
from flask_package import login_manager

# User session management
from flask_login import UserMixin

#user session management
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique = True , nullable=False)
    email = db.Column(db.String(120), unique = True , nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default ='default.jpg')
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"