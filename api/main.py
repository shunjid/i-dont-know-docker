from flask import Flask
from flask_cors import CORS
from constants.common import CONFIGURATION
from services.database import db
from controllers.users import users

# configuration
app = Flask(__name__)
app.config[CONFIGURATION["track"]] = False
app.config[CONFIGURATION["uri"]] = CONFIGURATION["sqlite"]
db.init_app(app)

# enable cors
CORS(app=app)

# migrate models to database
with app.app_context():
    db.create_all()

# register blueprints
app.register_blueprint(users)

if __name__ == "__main__":
    app.run(debug=True, host=CONFIGURATION["host"])
