# installed libraries
from flask import Blueprint, request
from marshmallow import ValidationError

# custom libraries
from constants.messages import ERRORS
from schema.user import UserSchema
from services.queries.user import (
    findAll,
    findOne,
    findByEmail,
    findByMobile,
    findByEmailExcludeId,
    findByMobileExcludeId,
)
from services.commands import create_one, commit
from services.instance import create_user_instance
from utils.response import success, error, success_dict


# global variables
users_bp = Blueprint("users", __name__)
user_schema = UserSchema()


@users_bp.route("/api/users", methods=["GET"])
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


@users_bp.route("/api/users/<id>", methods=["GET"])
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


@users_bp.route("/api/users", methods=["POST"])
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


@users_bp.route("/api/users/<id>", methods=["PUT"])
def update_user(id):
    try:
        # check user exists
        user = findOne(id)
        if user is None:
            return error(
                message=ERRORS["USER_NOT_FOUND"],
                status_code=404,
            )

        # validate body as per schema definition
        body = request.get_json()
        validated_user: dict = user_schema.load(body)
        updated_user = create_user_instance(validated_user)

        # unique key validation
        if findByEmailExcludeId(email=updated_user.email_address, user_id=id):
            return error(
                message=ERRORS["EMAIL_EXISTS"],
                status_code=500,
            )
        elif findByMobileExcludeId(mobile=updated_user.mobile_number, user_id=id):
            return error(
                message=ERRORS["MOBILE_EXISTS"],
                status_code=500,
            )
        else:
            user.first_name = updated_user.first_name
            user.last_name = updated_user.last_name
            user.email_address = updated_user.email_address
            user.mobile_number = updated_user.mobile_number
            commit()

            return success(data=user)

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
