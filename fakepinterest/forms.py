from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class Form_sign_in(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirm = SubmitField("Entrar")

class Form_login(FlaskForm):
    username = StringField("Nome de usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    senha_confirmacao = PasswordField("Confirme a senha", validators=[DataRequired(), EqualTo('senha')])
    botao_confirm = SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Por favor, escolha outro.")
        
class Form_Foto(FlaskForm):
    foto = FileField("Foto URL", validators=[DataRequired()])
    botao_confirm = SubmitField("Enviar Foto")
    