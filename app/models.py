from . import db
from werkzeug.security import generate_password_hash

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_title = db.Column(db.String(100))
    property_description = db.Column(db.String(256))
    property_no_rooms = db.Column(db.Integer)
    property_no_bathrooms = db.Column(db.Float)
    property_price = db.Column(db.Float)
    property_type = db.Column(db.String(50))
    property_location = db.Column(db.String(255))
    property_filename = db.Column(db.String(255))

    def __init__(self, property_title, property_description, property_no_rooms, property_no_bathrooms, property_price, property_type, property_location,property_filename):
        self.property_title = property_title
        self.property_description = property_description
        self.property_no_rooms = property_no_rooms
        self.property_no_bathrooms = property_no_bathrooms
        self.property_price = property_price
        self.property_type = property_type
        self.property_location = property_location
        self.property_filename = property_filename

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)