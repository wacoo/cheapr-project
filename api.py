from flask import Blueprint, jsonify, request, url_for
from models.engine.file_storage import Storage
from models.user import User

api = Blueprint(__name__, "api")
storage = Storage()

@api.errorhandler(404)
def page_not_found(e):
    res = jsonify({'status': 404, 'error': 'not found'})
    res.status_code = 404
    return res

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
    data = storage.get(cls, id)    
    return jsonify(data.__dict__)

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
@api.route("/add/user", methods=["GET", "POST"])
def add_user():
    """ add new user """
    fname = request.form.get("rfname")
    mname = request.form.get("rmname")
    lname = request.form.get("rlname")
    uname = request.form.get("runame")
    passwd = request.form.get("rpwd")
    cpasswd = request.form.get("rcpwd")
    city = request.form.get("rcity")
    utype = request.form.get("rtype")
    gps = request.form.get("rlocation")

    if passwd == cpasswd and passwd:
        user = User()
        user.firstname = fname
        user.middlename = mname
        user.lastname = lname
        user.username = uname
        user.password = passwd
        user.city = city
        user.location = gps
        user.active = True
        storage.reload()
        storage.new(user)
        return user.id
    else:
        return "Failed!"

@api.route("/add/shop", methods=["GET", "POST"])
def add_shop():
    return

@api.route("/add/product_service", methods=["GET", "POST"])
def add_product_service():
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