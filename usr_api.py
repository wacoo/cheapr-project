from flask import Blueprint, render_template,redirect, url_for, request, make_response, jsonify, message_flashed, session
from models.engine.file_storage import Storage
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context

auth = HTTPBasicAuth()
storage = Storage()
login = Blueprint('login', __name__)
@login.route('/')
def index():
    return 'Index'

@login.route('/profile')
#@auth.login_required
def profile():    
    return make_response(jsonify({'status': "Login Succuss!"}), 200)

@login.route('/user_profile')
@auth.login_required
def profile_page():
    user = request.args['user']
    return render_template('profile.html', usr = user)

@login.route('/login')
def log():
    if session['logged_in'] != None:
        return redirect(url_for('login.profile_page', user = session['user']))
    return render_template('login.html')

@login.route('/login', methods=['POST'])
def login_post():
    
    """ verify user """ 
    data = request.get_json()    
    uname = data["lusname"]
    passwd = data["lpwd"]
    storage.reload()

    pass1 = storage.getpass(uname)
    print(pass1)
    if verifyPassword(pass1, passwd):
        session['user'] = uname
        session['logged_in'] = True
        return redirect('login.profile_page', user = session['user'])
    else:
        return make_response(jsonify({'status': "Wring password"}), 401)

@login.route('/signup')
def signup():
    return render_template('register.html')

@login.route('/signup', methods=['POST'])
def signup_post():
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
        user.password = pwd_context.encrypt(passwd)
        user.city = city
        user.usertype = utype
        user.gps_location = gps
        user.active = False
        user.photo = photo
        storage.reload()
        print(user.password)
        if storage.new(user):

            return make_response(jsonify({'user id': user.id}), 200)
        else:
            return make_response(jsonify({'status': 'error'}), 500)
    else:
        return make_response(jsonify({'status': 'user.id'}), 400)
    

@login.route('/logout')
def logout():
    session.clear()
    print("Logout Success!")
    return 'Logout'

@auth.verify_password
def verifyPassword(upass, hpass):
    if (pwd_context.verify(upass, hpass)):
        return True
    else:
        return False