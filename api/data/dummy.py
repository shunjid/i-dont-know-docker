# do not execute here.
# take these under context of main.py

from services import db
from models.user import User

db.session.add(
    User(
        first_name="Test",
        last_name="Doe",
        email_address="test@example.com",
        mobile_number="+8801172211111",
    )
)

db.session.commit()
