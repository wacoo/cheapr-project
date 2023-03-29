from flask import Blueprint, render_template
from models.engine.file_storage import Storage
from usr_api import auth
views = Blueprint(__name__, "views")
@views.route("/")
def home():
    return render_template("index.html", login_type = "login", login_type_txt = 'Login')
    #print(session)
    ##if session['user']:
     #       return render_template("index.html", login_type = "logout", login_type_txt = 'Login')
    #    else:
    #return render_template("index.html", login_type = "login", login_type_txt = 'Login')
        #else:    
@views.route("/shops")
def shops():
    return render_template("shops.html", cls_shop="active")
@views.route("/goods")
def goods():  
    return render_template("goods.html", cls_good="active")

@views.route("/services")
def services():  
    return render_template("services.html", cls_serv="active")

@views.route("/promos")
def promos():  
    return render_template("promotions.html", cls_promo="active")

@views.route("/register")
@auth.login_required
def register():  
    return render_template("register.html", cls_promo="active")

@views.route("/login")
def login():  
    return render_template("login.html", cls_promo="active")

@views.route("/add_shop")
@auth.login_required
def add_shop():  
    return render_template("add_shop.html", cls_promo="active")

@views.route("/add_product")
@auth.login_required
def add_product():  
    return render_template("add_product.html", cls_promo="active")
@views.route("/add_service")
@auth.login_required
def add_service():  
    return render_template("add_service.html", cls_promo="active")