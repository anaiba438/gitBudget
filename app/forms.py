from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class BForm(FlaskForm):
    income = FloatField('Income', validators=[DataRequired()])
    rent = StringField('Rent', validators=[DataRequired()])
    groceries = StringField('Groceries', validators=[DataRequired()])
    transport = StringField('Transport', validators=[DataRequired()])
    entertainment = FloatField('Entertainment')
    eatingout = FloatField('Eating out')
    other = FloatField('Other')
    submit = SubmitField('Add Input')

    
