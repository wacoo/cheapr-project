from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", cls_home="active")

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
def register():  
    return render_template("register.html", cls_promo="active")

@views.route("/login")
def login():  
    return render_template("login.html", cls_promo="active")

@views.route("/add_shop")
def add_shop():  
    return render_template("add_shop.html", cls_promo="active")

@views.route("/add_product")
def add_product():  
    return render_template("add_product.html", cls_promo="active")
@views.route("/add_service")
def add_service():  
    return render_template("add_service.html", cls_promo="active")