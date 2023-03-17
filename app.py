from flask import Flask
from views import views
from api import api
app = Flask(__name__)
app.url_map.strict_slashes =True
app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(api, url_prefix="/api/v1")
if __name__ == '__main__':
    app.run(debug=True)