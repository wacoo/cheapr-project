from flask import Flask, make_response, jsonify, current_app
from models.engine.file_storage import Storage
from views import views
from api import api
from flask_cors import CORS
from usr_api import login
import os

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(api, url_prefix="/api/v1")
app.register_blueprint(login, url_prefix="/user")
app.url_map.strict_slashes =True
app.secret_key = 'this is  not a good secret key'

UPLOAD_FOLDER = 'static/images/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024
storage = Storage()

def load_user(user_id):
    storage.reload()
    return storage.getpass(user_id)
with app.app_context():
    print (current_app.name)
@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'status': 'Not found'}), 404)

@app.errorhandler(400)
def bad_req(e):
    return make_response(jsonify({'status': 'Bad request'}), 400)

@app.errorhandler(500)
def server_error(e):
    return make_response(jsonify({'status': 'Server error'}), 500)
    
if __name__ == '__main__':
    app.run(debug=True)   