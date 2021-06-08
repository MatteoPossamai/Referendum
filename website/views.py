  
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html")