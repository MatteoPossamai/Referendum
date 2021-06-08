from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name =request.form.get("username")
        psw =request.form.get("psw")
        user = User.query.filter_by(name=name).first()
        if user:
            if psw == user.password:
                flash("Logged succesfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Unexistent user", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        username=request.form.get('username')
        psw1=request.form.get('psw1')
        psw2=request.form.get('psw2')

        user = User.query.filter_by(name=username).first()
        if user:
            flash("Username already exist", category="error")
        elif len(username)<3:
            flash("Username too short", category="error")
        elif psw1!=psw2:
            flash("Passwords are different", category="error")
        else:
            new_user = User(name=username, password=psw1)
            print(new_user)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created", category="Success")
            return redirect(url_for("views.home"))
    return render_template("signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
