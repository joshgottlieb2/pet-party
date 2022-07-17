from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    pets = db.relationship('Pet', backref='user', lazy='dynamic')

    def get_user(self):
        return User.query.get(self.user_id)

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    description = db.Column(db.String(250))
    image_link = db.Column(db.String(250))
    date_adopted = db.Column(db.DateTime, default=datetime.utcnow())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)