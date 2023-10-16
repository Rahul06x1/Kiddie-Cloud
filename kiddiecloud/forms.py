from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from kiddiecloud.models import User, AddChildRight,Gallery , AddVaccination, AddHealthyDiet, AddSchool, AddBabyCare, BookDoctor, AddTalent, BookAdmission, AddComplaints,AddQuestions, AddParenting
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SelectField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    image = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=1, max=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),Length(min=1, max=8) ,EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self , username):
        excluded_chars = " *?!'^+%&/()=}][{$#0123456789"
        for char in self.username.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_email(self , email):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.email.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_password(self , password):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.password.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_confirm_password(self , confirm_password):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.confirm_password.data:
            if char in excluded_chars:
                raise ValidationError("invalid")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class Resetrequest(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')   

class Admingallery(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
    desc = StringField('Description',validators=[ Length(min=2, max=20)])
    image = FileField('Upload Picture', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submitt')
    def validate_name(self , name):
        excluded_chars = " *?!'^+%&/()=}][{$#0123456789"
        for char in self.name.data:
            if char in excluded_chars:
                raise ValidationError("invalid")


class Adminccount(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[Email()])
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')
    def validate_name(self , name):
        excluded_chars = " *?!'^+%&/()=}][{$#0123456789"
        for char in self.name.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_email(self , email):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.email.data:
            if char in excluded_chars:
                raise ValidationError("invalid")

class UserAccount(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[Email()])
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')
    def validate_name(self , name):
        excluded_chars = " *?!'^+%&/()=}][{$#0123456789"
        for char in self.name.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_email(self , email):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.email.data:
            if char in excluded_chars:
                raise ValidationError("invalid")

class DoctorAccount(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[Email()])
    address = StringField('Address')
    phone = StringField('Phone Number')
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')
    def validate_name(self , name):
        excluded_chars = " *?!'^+%&/()=}][{$#0123456789"
        for char in self.name.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_email(self , email):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.email.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_address(self , address):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.address.data:
            if char in excluded_chars:
                raise ValidationError("invalid")
    def validate_phone(self , phone):
        excluded_chars = " *?!'^+%&/()=}][{$#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in self.phone.data:
            if char in excluded_chars:
                raise ValidationError("invalid")


class Changepassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min=1, max=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),Length(min=1, max=8) ,EqualTo('password')])
    submit = SubmitField('Reset')