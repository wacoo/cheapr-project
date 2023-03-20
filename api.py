from flask import Blueprint, jsonify, request, url_for, make_response, abort
from models.engine.file_storage import Storage
from models.product import Product
from models.shop import Shop
from models.user import User
import json

api = Blueprint(__name__, "api")
storage = Storage()

""" GET """
@api.route("/", methods=["GET"], strict_slashes=False)
def all():
    """ show all objects """
    ls = []
    storage.reload()
    data = storage.all()
    for d in data.values():
        ls.append(d.__dict__)
    return jsonify(ls)

@api.route("/get/", methods=["GET"], strict_slashes=False)
def get():
    cls = request.args.get("cls")
    id = request.args.get("id")
    storage.reload()
    if id: 
        data = storage.get(cls, id)    
        return jsonify(data.__dict__)
    else:
        data = storage.getby(cls)
        return jsonify(data)

@api.route("/count", methods=["GET"], strict_slashes=False)
@api.route("/count/<cls>", methods=["GET"], strict_slashes=False)
def count(cls=None):
    """ return the number of objects """
    count = 0
    storage.reload()
    all = storage.all()
    if cls:
        for key in all.keys():
            cl = key.split(".")
            if cls == cl[0]:
                count += 1
    else:
        for key in all.keys():
            count += 1
    return jsonify({"count": count})

""" DELETE """
@api.route("/del/<uname>", methods=["GET", "DELETE"])
def delete(uname=None):
    """ remove object """
    if uname:
        storage.reload()
        for obj in storage.all().values():
            if uname == obj.__dict__["username"]:
                storage.delete(obj)
                storage.save()
                return jsonify({"result": "deleted"})
    return jsonify({"result": "not deleted"})

""" POST """
@api.route("/add/user", methods=["POST"])
def add_user():
    data = request.get_json()
    """ add new user """ 

    fname = data['rfname']
    mname = data["rmname"]
    lname = data["rlname"]
    uname = data["runame"]
    passwd = data["rpwd"]
    cpasswd = data["rcpwd"]
    city = data["rcity"]
    utype = data["rtype"]
    gps = data["rlocation"]

    if passwd == cpasswd and passwd:
        user = User()
        user.firstname = fname
        user.middlename = mname
        user.lastname = lname
        user.username = uname
        user.password = passwd
        user.city = city
        user.usertype = utype
        user.location = gps
        user.active = True
        storage.reload()
        if storage.new(user):
            return make_response(jsonify({'user id': user.id}), 200)
        else:
            return make_response(jsonify({'status': 'error'}), 500)
    '''else:
        return make_response(jsonify({'status': 'user.id'}), 400)'''

@api.route("/add/shop", methods=["POST"])
def add_shop():
    data = request.get_json()
    owner = data["sowner"]
    shop = data["sname"]
    type = data["stype"]
    product_service = data["pr_sv"] # TODO get this form db
    city = data["scity"]
    gps = data["rlocation"]
    shop1 = Shop()
    shop1.owner = owner
    shop1.name = shop
    shop1.type = type
    shop1.product_service = product_service
    shop1.city = city
    shop1.gps_location = gps
    storage.reload()
    if storage.new(shop1):
        return make_response(jsonify({'user id': shop1.id}), 200)
    else:
        return make_response(jsonify({'status': 'error'}), 500) #owner +", "+ shop +", " + type  +", " + product_service +", " + city  +", " + gps

    #return make_response(jsonify({'user id': data}), 200)

@api.route("/add/product", methods=["POST"])
def add_product():
    data = request.get_json()
    name = data["pname"]
    brand = data["pbrand"]
    model = data["pmodel"]
    category = data["pcategory"]
    man_date = data["pmdate"]
    status = data["pstatus"]
    quality = data["pquality"]
    price = data["pprice"]
    shop = data["pshop"]
    product = Product()
    product.name = name
    product.brand = brand
    product.model = model
    product.category =category
    product.manufature_date = man_date
    product.status = status
    product.quality = quality
    product.price = price
    product.shop = shop
    storage.reload()
    storage.new(product)
    if storage.new(product):
        return make_response(jsonify({'user id': product.id}), 200)
    else:
        return make_response(jsonify({'status': 'error'}), 500)

    return

@api.route("/add/promotion", methods=["GET", "POST"])
def add_promotion():
    return

""" PUT/UPDATE """
@api.route("/update/user", methods=["GET", "PUT"])
def update_user():
    return
@api.route("/update/shop", methods=["GET", "PUT"])
def update_shop():
    return
@api.route("/update/product_service", methods=["GET", "PUT"])
def update_product_service():
    return
@api.route("/update/promotion", methods=["GET", "PUT"])
def update_promotion():
    return