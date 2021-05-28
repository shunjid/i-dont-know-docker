from flask import Blueprint
from models.user import User
from utils.response import success, error

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
