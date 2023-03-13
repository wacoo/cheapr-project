from flask import Blueprint, render_template, redirect

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