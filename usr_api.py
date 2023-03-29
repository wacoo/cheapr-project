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
    user = session['user']   
    return make_response(jsonify({'status': "Login Succuss!", 'user': user}), 200)

@login.route('/user_profile')
@auth.login_required
def profile_page():
    #user = session['user']
    return render_template('profile.html')

@login.route('/login', methods=['GET'])
def log():
    return render_template('login.html')
    '''if session['logged_in']:
            uname = session['user']           
            return redirect(url_for('login.profile', user = uname))
        else:'''            
    
@login.route('/login', methods=['POST'])
@auth.login_required
def login_post():
    
    """ verify user """
    return redirect(url_for('login.profile'))
    '''else:
        return make_response(jsonify({'status': "Wrong password"}), 401)'''

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
        user.password = generate_password_hash(passwd)
        user.city = city
        user.usertype = utype
        user.gps_location = gps
        user.active = False
        user.photo = photo
        storage.reload()
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
def verifyPassword(username, password):
    print(username +'='+ password)
    storage.reload()
    hashed = storage.getpass(username)
    if username and check_password_hash(hashed, password):        
        session['user'] = username
        return True
    elif 'user' in session.keys():
        if session['user']:
            print(username +'C='+ password)
            return True
        else:
            return False
    else:
        return False

def getSession():
    ''' return current session'''
    return session['user']