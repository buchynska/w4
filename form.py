from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from wtforms import validators, ValidationError

class userForm(Form):


    user_name = StringField('user_name: ',[validators.DataRequired('Please enter user_name.')])
    user_age = IntegerField('user_id: ',[validators.DataRequired('Please enter user_id.'),
                                           validators.NumberRange(0,100,'You are wrong')])


    submit = SubmitField('Submit')
