from services.database import db


def commit():
    db.session.commit()


def create_one(instance):
    db.session.add(instance)
    commit()


def delete_one(instance):
    db.session.delete(instance)
    commit()
