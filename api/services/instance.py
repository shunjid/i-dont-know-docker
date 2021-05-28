from models.user import User


def create_user_instance(schema: dict):
    return User(
        first_name=schema["firstName"],
        last_name=schema["lastName"],
        email_address=schema["emailAddress"],
        mobile_number=schema["mobileNumber"],
    )
