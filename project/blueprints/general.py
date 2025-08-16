from flask import Blueprint,render_template
from extentions import * 
from models.User import User
from sqlalchemy import desc,asc

general=Blueprint("general_blueprint",__name__)

@general.route('/')
def home():
    top_users=User.query.order_by(desc(User.tasks_count)).limit(3).all()
    new_users=User.query.order_by(asc(User.tasks_count)).limit(3).all()
    return render_template("home.html",top_users=top_users,new_users=new_users)


@general.route('/about')
def about():
    return render_template("about.html")