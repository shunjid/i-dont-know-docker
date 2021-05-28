from services.database import db


def create_one(instance):
    db.session.add(instance)
    db.session.commit()
