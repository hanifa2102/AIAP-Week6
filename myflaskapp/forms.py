from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("Pls put the url of your image",[validators.Required("Please enter  your name.")])
    submit = SubmitField("Send")
