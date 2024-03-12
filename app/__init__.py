from flask import Flask
from .config import Config




#initlaize app
app = Flask(__name__)
from app import views

# Configuration settings
app.config.from_object(Config)

# Add any other configurations as needed

# Initialize the form
# my_form = MyForm()


