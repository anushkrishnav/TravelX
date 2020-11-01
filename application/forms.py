from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from .model.models import User


class EditProfileForm(FlaskForm):
    fname = StringField('Firstname')
    lname = StringField('Lastname')
    Adress = TextAreaField('Adress', validators=[Length(min=0, max=200)])
    City = StringField('City')
    Country = StringField('Country')
    Pincode = StringField('Pincode')
    About = TextAreaField('About me', validators=[Length(min=0, max=500)])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class EventsForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired()])
    Title = StringField('Party name', validators=[DataRequired()])
    EDate = StringField('Party Date', validators=[DataRequired()])
    Time = StringField('Party Time', validators=[DataRequired()])
    Meet = StringField('Meet/Zoom link', validators=[DataRequired()])
    submit = SubmitField('Start the Party')
