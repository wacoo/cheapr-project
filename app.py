from flask import Flask, make_response, jsonify
from views import views
from api import api
app = Flask(__name__)
app.url_map.strict_slashes =True
app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(api, url_prefix="/api/v1")

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