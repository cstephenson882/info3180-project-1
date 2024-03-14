
# new
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import InputRequired
from wtforms import SubmitField,SelectField,FloatField, TextAreaField
from werkzeug.utils import secure_filename


class MyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    property_description = TextAreaField('Description',  validators=[InputRequired()], render_kw={"class": "large-input"})

    property_no_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    property_no_bathrooms = FloatField('No. of Bathrooms', validators=[InputRequired()])

    property_price = IntegerField('Price', validators=[InputRequired()])
    choices = [('1', 'House'), ('2', 'Apartment')]
    property_type = SelectField('Property Type',choices=choices, default='1', validators=[InputRequired()])

    property_location = StringField('Location', validators=[InputRequired()])

    property_file = FileField('Add Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Add Property')



class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')

# to use add route to view.py and from .froms import MyForm 
# end new
