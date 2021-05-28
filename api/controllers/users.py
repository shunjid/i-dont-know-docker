from flask import Blueprint, request
from models.user import User
from utils.response import success, error, dict_to_json
from schema.user import UserSchema
from marshmallow import ValidationError

users = Blueprint("users", __name__)


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
    user_schema = UserSchema()

    try:
        user_validation_result = user_schema.load(body)
        print(type(user_validation_result))
        return dict_to_json(data=user_validation_result)
    except ValidationError as err:
        return error(message=err.messages, status_code=500)
