# installed libraries
from flask import Blueprint, request
from marshmallow import ValidationError

# custom libraries
from constants.messages import ERRORS
from schema.user import UserSchema
from services.queries.user import findAll, findOne, findByEmail, findByMobile
from services.commands import create_one
from services.instance import create_user_instance
from utils.response import success, error, success_dict


# global variables
users = Blueprint("users", __name__)
user_schema = UserSchema()


@users.route("/api/users", methods=["GET"])
def get_users():
    try:
        return success(
            data=findAll(),
            single=False,
        )
    except Exception as e:
        return error(
            message=str(e),
            status_code=404,
        )


@users.route("/api/users/<id>", methods=["GET"])
def get_user_by_id(id):
    try:
        return success(
            data=findOne(id),
        )
    except Exception as e:
        return error(
            message=ERRORS["USER_NOT_FOUND"],
            status_code=404,
        )


@users.route("/api/users", methods=["POST"])
def create_user():
    body = request.get_json()

    try:
        validated_user: dict = user_schema.load(body)
        new_user = create_user_instance(validated_user)

        if findByEmail(new_user.email_address):
            return error(
                message=ERRORS["EMAIL_EXISTS"],
                status_code=500,
            )
        elif findByMobile(new_user.mobile_number):
            return error(
                message=ERRORS["MOBILE_EXISTS"],
                status_code=500,
            )
        else:
            create_one(new_user)

            return success_dict(
                data=validated_user,
            )
    except ValidationError as err:
        return error(
            message=err.messages,
            status_code=500,
        )
    except Exception as e:
        return error(
            message=str(e),
            status_code=500,
        )
