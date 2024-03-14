
# ========= Configuration settings ==============
from flask import Flask
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)

# ======== Database setup start ================== 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db) 
# ======== Database setup end ==================== 


# Add any other configurations as needed

# Initialize the form
# my_form = MyForm()
from app import views

