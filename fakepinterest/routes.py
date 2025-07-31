from flask import render_template, url_for, redirect    
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import Form_sign_in, Form_login
from fakepinterest.models import Usuario, Foto

@app.route('/', methods=['GET', 'POST'])
def homepage():
    sign_in = Form_sign_in()
    if sign_in.validate_on_submit():
        user = Usuario.query.filter_by(email=sign_in.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, sign_in.senha.data): 
            login_user(user, remember=True)
            return redirect(url_for("perfilpage", id_user=user.id))
    return render_template("homepage.html", form=sign_in)



@app.route('/login', methods=['GET', 'POST'])
def create_account():
    login = Form_login()
    if login.validate_on_submit():
        senha = bcrypt.generate_password_hash(login.senha.data).decode('utf-8')
        bcrypt.check_password_hash(senha, login.senha.data)
        user = Usuario(
            username=login.username.data,
            email=login.email.data,
            senha=senha
        )
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("perfilpage", id_user=user.id))
    return render_template("login.html", form=login)



@app.route('/perfil/<id_user>')
@login_required
def perfilpage(id_user):
    if int(id_user) == int(current_user.id):
        return render_template("perfil.html", username=current_user)
    else:
        usuario = Usuario.query.get(int(id_user))
        return render_template("perfil.html", username=usuario)


@app.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for("homepage"))