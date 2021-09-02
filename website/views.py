from typing_extensions import ParamSpecKwargs
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Refs

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    p1=0
    p2=0
    selected=0
    if request.method =="POST":
        selected = request.form.getlist('opt')
        if len(selected)>0:
            #print(selected,selected[:2]=='fa')
            Refs.query.filter_by(id=int(str(selected[0][2:]))).first().voters +=current_user.name +'#'
            if str(selected[0][:2])=='fa':
                Refs.query.filter_by(id=int(str(selected[0][2:]))).first().fVote+=1
            elif str(selected[0][:2])=='sa':
                Refs.query.filter_by(id=int(str(selected[0][2:]))).first().sVote+=1
            db.session.commit()
        else:
            flash('You must choose an answer to submit')
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
        #print(question, fAnsw, sAnsw)
        if sAnsw and fAnsw and question:
            newRef = Refs(question=question, fAnsw=fAnsw, sAnsw=sAnsw, user_name=current_user.name)
            db.session.add(newRef)
            db.session.commit()
            flash('Refs created correctly', category='success')
            return redirect(url_for("views.home"))
        else:
            flash('Not all pitches completed', category='error')
    return render_template("createPage.html", user=current_user, datas=Refs.query)