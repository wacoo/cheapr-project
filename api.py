from flask import Blueprint, jsonify, request, make_response, abort, current_app
from models.engine.file_storage import Storage
from models.product import Product
from models.service import Service
from models.shop import Shop
from models.user import User
#from app import app
from werkzeug.utils import secure_filename
import os

api = Blueprint(__name__, "api")
storage = Storage()
UPLOAD_FOLDER = 'static/images/upload'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg', 'gif'}
def allowed_file(filename):
    """ check file extension """
    sp = filename.split('.').lower()
    if sp[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False  
    
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
    uname = data["rusname"]
    passwd = data["rpwd"]
    cpasswd = data["rcpwd"]
    city = data["rcity"]
    utype = data["rtype"]
    gps = data["rlocation"]
    photo = data["pphoto_name"]

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
        user.photo = photo
        storage.reload()
        if storage.new(user):
            return make_response(jsonify({'user id': user.id}), 200)
        else:
            return make_response(jsonify({'status': 'error'}), 500)
    else:
        return make_response(jsonify({'status': 'user.id'}), 400)

@api.route("/add/shop", methods=["POST"])
def add_shop():
    data = request.get_json()
    owner = data["sowner"]
    shop = data["sname"]
    type = data["stype"]
    product_service = data["pr_sv"] # TODO get this form db
    city = data["scity"]
    gps = data["rlocation"]
    photo = data["pphoto_name"]

    shop1 = Shop()
    shop1.owner = owner
    shop1.name = shop
    shop1.type = type
    shop1.product_service = product_service
    shop1.city = city
    shop1.gps_location = gps
    shop1.photo = photo
    storage.reload()
    if storage.new(shop1):
        return make_response(jsonify({'user id': shop1.id}), 200)
    else:
        return make_response(jsonify({'status': 'error'}), 500) #owner +", "+ shop +", " + type  +", " + product_service +", " + city  +", " + gps

    #return make_response(jsonify({'user id': data}), 200)

@api.route("/add/photo", methods=["POST"])
def add_photo():
    if 'pphoto' not in request.files:
        return make_response(jsonify({'message': 'No file part in request'}), 400)
    photo = request.files["pphoto"]
    if photo.filename == '':
        return make_response(jsonify({'message': 'No file file selected for upload'}), 400)
    if photo: #and allowed_file(photo.filename):
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'fn':filename});#make_response(jsonify({'status': 'upload success'}), 200);

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
    photo = data["pphoto_name"]

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
    product.photo = photo
    storage.reload()
    storage.new(product)
    if storage.new(product):
        return make_response(jsonify({'user id': data}), 200)
    else:
        return make_response(jsonify({'status': 'error'}), 500)

@api.route("/add/service", methods=["POST"])
def add_service():
    data = request.get_json()    
    name = data["sname"]
    category = data["scategory"]
    price = data["sprice"]
    provider = data["sprovider"]
    #TODO need quality here    
    photo = data["pphoto_name"]

    service = Service()
    service.name = name
    service.price =price
    service.category = category
    service.provider = provider
    service.photo = photo
    storage.reload()
    storage.new(service)
    if storage.new(service):
        return make_response(jsonify({'user id': data}), 200)
    else:
        return make_response(jsonify({'status': 'error'}), 500)
    
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