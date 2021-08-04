from flask import Flask


def criar_app():

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = "DFNJHFKDK"

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

    