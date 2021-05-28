from flask import jsonify, Blueprint
from models.user import User

users = Blueprint("users", __name__)


@users.route("/api/users", methods=["GET"])
def index():
    response = dict()
    try:
        all_users = User.query.all()

        response["status"], response["data"] = "ok", [
            user.to_dict() for user in all_users
        ]
    except Exception as e:
        response["status"], response["message"] = "failed", str(e)
    finally:
        return jsonify(response)
