from flask import render_template, url_for, redirect    
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import Form_sign_in, Form_login, Form_Foto
from fakepinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename



#pagina inicial
@app.route('/', methods=['GET', 'POST'])
def homepage():
    sign_in = Form_sign_in()
    if sign_in.validate_on_submit():
        user = Usuario.query.filter_by(email=sign_in.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, sign_in.senha.data): 
            login_user(user, remember=True)
            return redirect(url_for("feedpage"))
    return render_template("homepage.html", form=sign_in)



#pagina de login
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
        return redirect(url_for("feedpage"))
    return render_template("login.html", form=login)



#Pagina de perfil
@app.route('/perfil/<id_user>', methods=['GET', 'POST'])
@login_required
def perfilpage(id_user):
    if int(id_user) == int(current_user.id):
        #Usuario esta vendo o proprio perfil
        form_foto = Form_Foto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_arquivo = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_arquivo)
            arquivo.save(caminho)

            # Salvar a foto no banco de dados
            foto = Foto(imagem=nome_arquivo, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template("perfil.html", username=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_user))
        return render_template("perfil.html", username=usuario, form=None)




@app.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for("homepage"))



@app.route('/feed')
@login_required
def feedpage():
    fotos = Foto.query.order_by(Foto.data_cracao.desc()).all()
    return render_template("feed.html", fotos=fotos)