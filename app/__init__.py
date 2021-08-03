from flask import Flask


def criar_app():

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = "DFNJHFKDK"

    return app

    