from flask import Blueprint, render_template
from models.engine.file_storage import Storage
from usr_api import auth
views = Blueprint(__name__, "views")
@views.route("/")
def home():
    """ open home page """
    return render_template("index.html")
  
@views.route("/shops")
def shops():
    """ open shops page """
    return render_template("shops.html", cls_shop="active")

@views.route("/goods")
def goods():
    """ open goods page """
    return render_template("goods.html", cls_good="active")

@views.route("/services")
def services():
    """ open services page """ 
    return render_template("services.html", cls_serv="active")

@views.route("/add_shop")
@auth.login_required
def add_shop():
    """ open add shop page """
    return render_template("add_shop.html", cls_promo="active")

@views.route("/add_product")
@auth.login_required
def add_product():
    """ open add product page """ 
    return render_template("add_product.html", cls_promo="active")

@views.route("/add_service")
@auth.login_required
def add_service():
    """ open add service page """ 
    return render_template("add_service.html", cls_promo="active")