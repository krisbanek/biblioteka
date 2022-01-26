from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField

class BookForm(FlaskForm):
    tytul = StringField()
    autor = StringField()
    przeczytane = BooleanField()
 