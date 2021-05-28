from services.database import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    mobile_number = db.Column(db.String(20), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        user_dict = {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email_address,
            "mobile": self.mobile_number,
        }

        return user_dict
