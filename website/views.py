from typing_extensions import ParamSpecKwargs
from flask import Blueprint, render_template, request, flash, redirect, url_for, request
from flask_login import login_required, current_user
from . import db
from .models import Refs

views = Blueprint('views', __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    if request.method =="POST":
        pass
    return render_template("home.html", user=current_user, datas=Refs.query)

@views.route("/create", methods=["GET","POST"])
@login_required
def create():
    if request.method=="POST":
        #Qua ci sarà la gestione dell'input dato dal form
        #la memorizzazione dei dati nel db, e il reindirizzamento
        #alla home, dove mediante Jinja vengono visualizzati
        question = request.form.get('question')
        fAnsw = request.form.get('answ1')
        sAnsw = request.form.get('answ2')
        print(question, fAnsw, sAnsw)
        if sAnsw and fAnsw and question:
            newRef = Refs(question=question, fAnsw=fAnsw, sAnsw=sAnsw, user_name=current_user.name)
            db.session.add(newRef)
            db.session.commit()
            flash('Refs created correctly', category='success')
            return redirect(url_for("views.home"))
        else:
            flash('Not all pitches completed', category='error')
    return render_template("createPage.html", user=current_user, datas=Refs.query)