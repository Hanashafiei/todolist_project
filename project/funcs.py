from flask import session
from models.User import User

def get_user():
    username=session.get("login")
    if username==None:
        return False
    return User.query.filter(User.user_name==username).first()