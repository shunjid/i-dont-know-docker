from flask import Flask, jsonify
from flask_cors import CORS
from services.database import db
from models.user import User

# initiate flask app
app = Flask(__name__)
# config
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# add database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usersdb.sqlite"
# initialize database
db.init_app(app)
# enable cors
CORS(app=app)

# migrate models to database
with app.app_context():
    db.create_all()


@app.route("/api/users", methods=["GET"])
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
