from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField

class ToDoForm(FlaskForm):
    tytul = StringField()
    autor = StringField()
    przeczytane = BooleanField()
 