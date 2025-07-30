from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import Form_sign_in, Form_login

@app.route('/', methods=['GET', 'POST'])
def homepage():
    sign_in = Form_sign_in()
    return render_template("homepage.html", form=sign_in)

@app.route('/login', methods=['GET', 'POST'])
def create_account():
    login = Form_login()
    return render_template("login.html", form=login)

@app.route('/perfil/<username>')
@login_required
def perfilpage(username):
    return render_template("perfil.html", username=username)