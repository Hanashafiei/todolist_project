from flask import Flask
from config import *
from flask_wtf.csrf import CSRFProtect
from extentions import *
from blueprints.general import general
from blueprints.login import login
from blueprints.panel import panel

app=Flask(__name__)
app.secret_key=SECRET_KEY
csrf=CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI']=MYSQL_CONFIG
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db.init_app(app)



app.register_blueprint(general)
app.register_blueprint(login,url_prefix="/login")
app.register_blueprint(panel,url_prefix="/panel")


if __name__=="__main__":
    app.run(debug=True,port=1010)
    