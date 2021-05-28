from flask import Blueprint, request
from models.user import User
from utils.response import success, error, success_dict
from schema.user import UserSchema
from marshmallow import ValidationError
from services.database import db

users = Blueprint("users", __name__)
user_schema = UserSchema()


@users.route("/api/users", methods=["GET"])
def get_users():
    try:
        all_users = User.query.all()
        return success(data=all_users, single=False)
    except Exception as e:
        return error(message=str(e), status_code=500)


@users.route("/api/users/<id>", methods=["GET"])
def get_user_by_id(id):
    try:
        user = User.query.get(id)

        if not user:
            return error("User not found")
        else:
            return success(data=user)
    except Exception as e:
        return error(message=str(e), status_code=500)


@users.route("/api/users", methods=["POST"])
def create_user():
    body = request.get_json()

    try:
        # model validation
        schema = user_schema.load(body)

        new_user = User(
            first_name=schema["firstName"],
            last_name=schema["lastName"],
            email_address=schema["emailAddress"],
            mobile_number=schema["mobileNumber"],
        )

        # unique key validation
        email_exists = User.query.filter_by(
            email_address=new_user.email_address
        ).first()

        mobile_exists = User.query.filter_by(
            mobile_number=new_user.mobile_number
        ).first()

        if email_exists:
            return error(
                message="User already exists with this email",
                status_code=500,
            )
        elif mobile_exists:
            return error(
                message="User already exists with this mobile",
                status_code=500,
            )
        else:
            db.session.add(new_user)
            db.session.commit()
            return success_dict(data=schema)

    except ValidationError as err:
        return error(message=err.messages, status_code=500)

    except Exception as e:
        return error(message=str(e), status_code=500)
