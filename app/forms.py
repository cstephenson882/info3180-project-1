
# new
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import InputRequired
from wtforms import SubmitField

class MyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    property_description = StringField('Description', validators=[InputRequired()])

    property_no_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    property_no_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])

    property_price = IntegerField('Price', validators=[InputRequired()])
    property_type = StringField('Property Type', validators=[InputRequired()])

    property_location = StringField('Location', validators=[InputRequired()])
    
    submit = SubmitField('Add Property')

    

# to use add route to view.py and from .froms import MyForm 
# end new
