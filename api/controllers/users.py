from flask import Blueprint, request
from marshmallow import ValidationError
from models.user import User
from utils.response import success, error, success_dict
from schema.user import UserSchema
from services.user_queries import findAll, findOne, findByEmail, findByMobile
from services.commands import create_one

users = Blueprint("users", __name__)
user_schema = UserSchema()


@users.route("/api/users", methods=["GET"])
def get_users():
    try:
        return success(data=findAll(), single=False)
    except Exception as e:
        return error(message=str(e), status_code=500)


@users.route("/api/users/<id>", methods=["GET"])
def get_user_by_id(id):
    try:
        return success(data=findOne(id))
    except Exception as e:
        return error(message="User not found", status_code=404)


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

        if findByEmail(new_user.email_address):
            return error(
                message="User already exists with this email",
                status_code=500,
            )
        elif findByMobile(new_user.mobile_number):
            return error(
                message="User already exists with this mobile",
                status_code=500,
            )
        else:
            create_one(new_user)
            return success_dict(data=schema)

    except ValidationError as err:
        return error(message=err.messages, status_code=500)

    except Exception as e:
        return error(message=str(e), status_code=500)
