from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)




@views.route('/')
@views.route('Index')
def index ():
    return render_template ('index.html')
