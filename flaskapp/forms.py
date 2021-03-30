from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskapp.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Istifadeci Adi',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Parol', validators=[DataRequired()])
    confirm_password = PasswordField('Tekrar Parol',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Bu istifadeci adi mövcuddur xahis edirik başqa email daxil edin!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Bu email mövcuddur xahis edirik başqa ad daxil edin!')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Parol', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Istifadeci Adi',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    picture = FileField('Profil Seklini Yenile', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Bu istifadeci adi mövcuddur xahis edirik başqa email daxil edin!')

    def validate_email(self, email):
        if username.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Bu email mövcuddur xahis edirik başqa ad daxil edin!')




class PostForm(FlaskForm):
    title = StringField('Basliq', validators=[DataRequired()])
    content = TextAreaField('Movzu', validators=[DataRequired()])
    submit = SubmitField('Post')