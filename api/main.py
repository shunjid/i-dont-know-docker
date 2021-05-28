from flask import Flask
from flask_cors import CORS
from services.database import db
from routes.users import users

# configuration
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usersdb.sqlite"
db.init_app(app)

# enable cors
CORS(app=app)

# migrate models to database
with app.app_context():
    db.create_all()

# register blueprints
app.register_blueprint(users)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
