from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/perfil/<username>')
@login_required
def perfilpage(username):
    return render_template("perfil.html", username=username)