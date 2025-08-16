from flask import Blueprint,render_template,redirect,url_for,request,flash,session
import hashlib
from extentions import *
from sqlalchemy import and_
from models.User import User






login=Blueprint("login_blueprint",__name__)

@login.route('/')
def home():
    return render_template("login.html")


@login.route('/register', methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    confirm_password=request.form["confirm_password"]

    if password != confirm_password:
        flash("password not correct")
        return redirect(url_for("login_blueprint.home"))
    


    check_user=User.query.filter(User.user_name==username).first()
    if (check_user != None ):
         flash("username not correct")
         return redirect(url_for("login_blueprint.home"))
    
    new_user=User(user_name=username,password=hashlib.sha256(password.encode()).hexdigest())
    db.session.add(new_user)
    db.session.commit()

    flash("Ok")
    return redirect(url_for("login_blueprint.home"))
    


@login.route('/do_login',methods=["POST"])
def do_login():
   username = request.form["username"]
   password = request.form["password"]

   user=User.query.filter(and_(User.user_name==username,User.password==hashlib.sha256(password.encode()).hexdigest())).first()
   if (user==None):
       flash("username or password is wrong")
       return redirect(url_for("login_blueprint.home"))
   
   session['login']=username
   return redirect(url_for('panel_blueprint.home'))

