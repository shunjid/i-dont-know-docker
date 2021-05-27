from flask import Flask, jsonify
from flask_cors import CORS
from data.constants import users

# initiate flask app
app = Flask(__name__)

# enable cors
CORS(app=app)


def obj_dict(obj):
    return obj.__dict__


@app.route("/api/users", methods=["GET"])
def index():
    users_dict = {"status": "ok", "data": [obj.to_dict() for obj in users]}
    return jsonify(users_dict)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
