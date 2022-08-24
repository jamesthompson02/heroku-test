from flask import Blueprint

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return "<h1>Welcome to the Index Page</h1>"
